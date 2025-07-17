# MINDSCAPE 1 | WRO - FUTURE ENGINEERS | MINDSCAPE ACADEMY

## Team Members 🦋:
Maria Ghanem <br>
Charbel Ghanem <br>
Marc Zgheib <br>

<img src="" alt="team image" >


## Content 🤔:
| Folder | Content | 
| -- | -- |
| [Team Photos](Team%20Photos)| [Official team photo](/Team%20Photos/Official%20Team%20Photo.jpg), [Funny team photo](/Team%20Photos/Funny%20Team%20Photo.jpg) |
| [Vehicle Photos](Vehicle%20Photos) | [Bottom view](/Vehicle%20Photos/bottom.jpg), [front view](/Vehicle%20Photos/front.jpg), [left view](/Vehicle%20Photos/left.jpg), [rear view](/Vehicle%20Photos/rear.jpg), [right view](/Vehicle%20Photos/right.jpg), [top view](/Vehicle%20Photos/top.jpg) |
| [Models](Models) | [Final base model](/models/base%20v3.stl), [final camera base model](/models/camera%20base.stl), [final camera holder model](/models/camera%20holder%20v5.stl), [expansion board diagram](/models/expansion_board_diagram.png), [final fan holder model](/models/fan%20holder%20v2.stl), [old and unused models (zipped)](/models/old) |
| [Other](Other) | [Images used in documentation](other/images-used) |
| [Schemes](Schemes) | [Schematic explanations](/scheme/README.md), [expansion board schematic](/schemes/Raspberry%20Pi%20Expansion%20Board%20Schematic.png), [Raspberry Pi schematic](/schemes/Raspberry%20Pi%20Schematic.png), [vehicle schematic](/schemes/Vehicle%20Schematic.png) |
| [Src](Src) | [Obstacle challenge final](/src/ObstacleChallenge.py), [open challenge final](/src/OpenChallengeFinal.py), [HSV finder](/src/HSVRange.py), [test files](/src/Tests) |
| [Video](Video) | [Open challenge](/video/README.md), [obstacle challenge](/video/README.md) |

## Task 📔:

The self-driving car challenge in this season is a Time Attack race: there will not be multiple cars at the same time on the track. Instead, one car per attempt will try to achieve the best time by driving several laps fully autonomously in two different challenges.

**OBJECTIVE:** Build an autonomous vehicle that can complete 3 laps per round of the two challenges, the open challenge and the obstacle challenge.


### Open Challenge 🗺️:

<img src='Other/Open%20Challenge%20Map_1.jpg' alt='map pick'><br>

<img src="Other/Open%20Challenge%20Map_2.jpg" alt='map pick'><br>
Open Challenge Field

In this challenge, the robot has to drive around the map for 3 laps without any obstacles in the way. Instead, the inner wall of the map varies in size for every round that the robot parcours. This requires the robot to have a dynamic code that is able to recognize the field it is operating in. 


### Obstacle Challenge 🔴🟢:

<img src='Other/Obstacle challenge.jpg' alt='map pic(obstacles)'><br>
Obstacle Challenge Field

To complete the second challenge, the robot must perform 3 full laps around the map with red and green "traffic signs" spread randomly across the canvas whilst driving in the correct lane around each one. In addition, the last block at the end of the second lap determines the direction that the robot continues in for its third lap. If that block was to be red, the robot has to continue in the opposite direction but, if that block was to be green, it continues as it is to then try to parallel park in the designated area at the end of lap 3. Keep in mind that the whole mission should be done without knocking down any of the traffic signs.

## Assembly Guide:
### Software:

**1. Raspberry Pi OS:**
- Download and install the official Raspberry Pi Imager from [https://www.raspberrypi.com/software/]

**2. Connecting to the Raspberry Pi 5:**
- This step can be done in 2 ways: <br>

    a. Using the MicroHDMI and USB 3.0 Ports:<br>
    - Connect the Raspberry Pi to a monitor using an HDMI cable with a MicroHDMI head. 
    - Use the USB 3.0 ports on the Raspberry Pi to connect a seperate mouse and keyboard.<br>

    b. Using a laptop as a display:<br>
    - Open the Raspberry Pi terminal and run `sudo raspi-config`.
    - Go to `Interface Options > VNC > Enable`.
    - Connect the laptop to the Pi via Ethernet cable.
    - Set a static IP Address on the Pi so that the laptop can easily connect to it using `sudo nano /etc/dhcpcd.conf`.
    - Save and reboot `sudo reboot`.
    - Find the `static IP` on your computer, if it isn't set, enter `arp -a` into Command Prompt.
    - Download and install `RealVNC` on your computer from [https://www.realvnc.com/en/connect/download/viewer/].
    - Launch RealVNC and enter the correct `IP` along with the Pi's `username` and `password`.
    - You should finally see your Raspberry Pi desktop.

    <br>

### Hardware:

**1. Measuring the Components:**<br>
- Take measurement of the different parts (Raspberry Pi, camera, DC motor, servo motor etc.) <br><br>

**2. 3D Modeling:**<br>
- Start by designing the [model]() of the chassis and transferring the files to the 3D printer for construction.<br><br>

**3. Chassis Construction:**<br>
- Obtain the different 3D printed parts of the chassis and glue them tightly together.<br><br>

**4. Add the DC Motor:**<br>
- Add the motor at the [bottom]() of the robot.
- Connect the axle with the wheels.<br><br>

**5. Add the Motor Driver:**<br>
- Place the motor on the front-left corner of the [chassis]()
- Connect the wires of the DC motor to the OUT1 and OUT2 screws of the driver.<br><br>

**6. Add the Servo Motor:**<br>
- Insert the servo motor through the designated opening at the front.
- Tightly secure the steering axle to it.<br><br>

**7. Add the Camera:**<br>
-  At the highest part of the chassis, install the camera:<br>
    - Remove the camera cable.
    - Place the camera in the correct position.
    - Connect the cable to the camera.<br><br>


**8. Add Cooling Fans:**<br>
- Above where the Raspberry goes, two 5V fans are secured in place to provide adequate cooling.<br><br>

**9. Install the Raspberry Pi:**<br>
- Place the Raspberry Pi in the correct orientation in the middle of the chassis making sure that the wiring can still be done.<br><br>

**10. Add the Power Supply:**<br>
- Add 3 battery packs around the [rear]() of the chassis.<br><br>

**11. Wiring the robot:**<br>
- Refer to the provided [schematic]() to properly wire the electrical components ensuring everything recieves the correct power supply and voltage.<br><br>

**12. Last Inspection:**<br>
- Make sure that all the components are placed correctly and secured tightly to their positions to avoid anything coming undone during the mission.<br><br>

**13. Running the Code:**<br>
- With the construction complete, upload all your code to the Raspberry Pi from the `Src` folder and test the code for proper functionality.<br><br>