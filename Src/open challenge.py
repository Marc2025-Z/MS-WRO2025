import cv2
import numpy as np
from picamera2 import Picamera2
import time
from gpiozero import AngularServo, PWMOutputDevice, DigitalOutputDevice

# ---------------- GPIO Pin Setup ----------------
servo_pin = 18
motor_forward_pin = 23
motor_backward_pin = 24
ena_pin = 17

enA = PWMOutputDevice(ena_pin)
forward = DigitalOutputDevice(motor_forward_pin)
backward = DigitalOutputDevice(motor_backward_pin)

# ---------------- Servo Configuration ----------------
MIN_ANGLE = -90
MAX_ANGLE = 90
MIN_PULSE = 0.5 / 1000
MAX_PULSE = 2.4 / 1000
servo = AngularServo(
    servo_pin,
    min_angle=MIN_ANGLE,
    max_angle=MAX_ANGLE,
    min_pulse_width=MIN_PULSE,
    max_pulse_width=MAX_PULSE
)

# ---------------- Camera Initialization ----------------
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"format": "RGB888", "size": (640, 480)})
picam2.configure(config)
picam2.start()
time.sleep(2)  # Let camera warm up

# ---------------- Motor Functions ----------------
def go_forward(speed):
    forward.on()
    backward.off()
    enA.value = speed

def go_backward(speed):
    forward.off()
    backward.on()
    enA.value = speed

def stop():
    forward.off()
    backward.off()
    enA.value = 0

# ---------------- Wall Bottom Detection ----------------
def align_to_left_wall(frame, target_value=10000, threshold=60):
    h, w, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)

    left_strip = binary[:, :int(w * 0.25)]
    left_intensity = cv2.countNonZero(left_strip)
    cv2.rectangle(frame, (int(w * 0.75), 0), (w, h), (255, 0, 0), 2)



    # ✅ Stop if no wall is detected
    if left_intensity < 500:  # Adjust this threshold if needed
        print("🚫 No wall detected! Stopping.")
        return None  # Signal to caller that no wall was seen

    diff = left_intensity - target_value
    sensitivity = 1000

    if abs(diff) < sensitivity:
        angle = 0  # Good distance
    elif diff > 0:
        angle = 7  # Too close → steer right
    else:
        angle = -7  # Too far → steer left

    print(f"Wall pixels: {left_intensity}, Correction: {angle}")
    return angle
    
def detect_wall_bottom(frame, threshold=60, ratio_thresh=0.02, draw=True):
    """
    Detects dark areas at the bottom of the frame representing walls.
    Returns True if any such area crosses the middle horizontal line.
    """
    h, w, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY_INV)

    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    wall_detected = False

    middle_line = int(h * (1 / 3))
    if draw:
        cv2.line(frame, (0, middle_line), (w, middle_line), (0, 255, 0), 2)

    for cnt in contours:
        if cv2.contourArea(cnt) < (h * w * ratio_thresh):
            continue

        bottom_point = tuple(cnt[cnt[:, :, 1].argmax()][0])
        bx, by = bottom_point

        if draw:
            cv2.line(frame, (0, by), (w, by), (0, 0, 255), 2)

        if by >= middle_line:
            wall_detected = True

    return wall_detected

# ---------------- Wall Too Close Check ----------------
def is_too_close_to_wall(frame, y_threshold=420):
    """
    Returns True if the bottom of any large wall blob is too close (near bottom of frame).
    """
    h, w, _ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) < (h * w * 0.02):
            continue
        bottom_point = tuple(cnt[cnt[:, :, 1].argmax()][0])
        _, by = bottom_point
        if by >= y_threshold:
            return True
    return False

# ---------------- Color Detection ----------------
def detect_color_patch(frame):
    """
    Detects blue or orange areas in the frame using HSV color space.
    Returns 'blue', 'orange', or None.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Orange
    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([25, 255, 255])
    orange_mask = cv2.inRange(hsv, lower_orange, upper_orange)

    # Blue
    lower_blue = np.array([100, 150, 50])
    upper_blue = np.array([130, 255, 255])
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    orange_detected = cv2.countNonZero(orange_mask) > 500
    blue_detected = cv2.countNonZero(blue_mask) > 500

    if orange_detected:
        print("🟠 Orange detected!")
        return 'orange'
    if blue_detected:
        print("🔵 Blue detected!")
        return 'blue'
    return None

# ---------------- Main Navigation Loop ----------------
corner_count = 0
MAX_CORNERS = 12
print("🟢 Starting wall detection...")
duration = 3
while corner_count < MAX_CORNERS:
    frame = picam2.capture_array()
    walls = detect_wall_bottom(frame)
    cv2.imshow("Wall Detection", frame)
    servo.angle=0
    go_forward(0.3)
    if walls == True:
        print(f"🚧 Wall bottom crossed the center line! (Corner {corner_count + 1})")
        color = detect_color_patch(frame)

        if color == 'blue':
            print("↪ Turning RIGHT...")
            servo.angle = 20
            go_forward(0.3)
            time.sleep(1.8)
            stop()
            time.sleep(0.5)

            # Check closeness after turn
            frame = picam2.capture_array()
            if is_too_close_to_wall(frame):
                print("🔁 Too close to wall after RIGHT turn. Backing up...")
                go_backward(0.3)
                time.sleep(0.7)
                stop()
                time.sleep(0.3)

            corner_count += 1

        elif color == 'orange':
            print("↩ Turning LEFT...")
            servo.angle = -20
            go_forward(0.3)
            time.sleep(1.8)
            stop()
            time.sleep(0.5)

            # Check closeness after turn
            frame = picam2.capture_array()
            if is_too_close_to_wall(frame):
                print("🔁 Too close to wall after LEFT turn. Backing up...")
                go_backward(0.3)
                time.sleep(0.7)
                stop()
                time.sleep(0.3)

            corner_count += 1

        else:
            print("🟡 No color detected, backing up slightly...")
            servo.angle = 0
            go_backward(0.3)
            time.sleep(1)
            stop()
            continue
        

        # Move forward slowly after turn until next wall
        servo.angle = 0
        print("⬆ Adjusting and moving forward...")
        start = time.time()
        
        while time.time() - start < duration:
            frame = picam2.capture_array()
            frame = cv2.flip(frame, 1)
            angle = align_to_left_wall(frame)
            servo.angle = angle

            go_forward(0.25)
            sleep(0.25)
            stop()
        
            if angle is None:
                servo.angle(0)
                go_forward(0.3)
                sleep(0.3)
            


        cv2.imshow("Left Wall Alignment", frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ---------------- End of Mission ----------------
print("✅ Passed 12 corners. Mission complete!")
stop()
cv2.destroyAllWindows()
picam2.close()