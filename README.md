# MINDSCAPE 1 | WRO - FUTURE ENGINEERS | MINDSCAPE ACADEMY

## Team Members 🦋:
Charbel Ghanem <br>
Marc Zgheib <br>
Maria Ghanem <br>

<img src="" alt="image error" >

## Content 🤔:
| Folder  | Content| 
| -- | -- |
| [Team Photos](/Team%20Photos)| [Official team photo](/Team%20Photos/Official%20Team%20Photo.jpg), [funny team photo](/Team%20Photos/Funny%20Team%20Photo.jpg) |
| [Vehicle Photos](/Vehicle%20Photos) | [Bottom view](/Vehicle%20Photos/bottom.jpg), [front view](/Vehicle%20Photos/front.jpg), [left view](/Vehicle%20Photos/left.jpg), [rear view](/Vehicle%20Photos/rear.jpg), [right view](/Vehicle%20Photos/right.jpg), [top view](/Vehicle%20Photos/top.jpg) |
| [models](/models) | [Final base model](/models/base%20v3.stl), [final camera base model](/models/camera%20base.stl), [final camera holder model](/models/camera%20holder%20v5.stl), [expansion board diagram](/models/expansion_board_diagram.png), [final fan holder model](/models/fan%20holder%20v2.stl), [old and unused models (zipped)](/models/old) |
| [other](/other) | [Images used in documentation](other/images-used) |
| [schemes](/schemes) | [Schematic explanations](/scheme/README.md), [expansion board schematic](/schemes/Raspberry%20Pi%20Expansion%20Board%20Schematic.png), [Raspberry Pi schematic](/schemes/Raspberry%20Pi%20Schematic.png), [vehicle schematic](/schemes/Vehicle%20Schematic.png) |
| [src](/src) | [Obstacle challenge final](/src/ObstacleChallenge.py), [open challenge final](/src/OpenChallengeFinal.py), [HSV finder](/src/HSVRange.py), [test files](/src/Tests) |
| [videos](/videos) | [Open challenge](/video/README.md), [obstacle challenge](/video/README.md) |

## Task 📔:

The self-driving car challenge in this season is a Time Attack race: there will not be multiple cars at the same time on the track. Instead, one car per attempt will try to achieve the best time by driving several laps fully autonomously in two different challenges.



### Open Challenge 🗺️:

<img src='' alt='map pick'>
Open Challenge Field

In this challenge, the robot has to drive around the map for 3 laps without any obstacles in the way. Instead, the inner wall of the map varies in size for every round that the robot parcours. This requires the robot to have a dynamic code that is able to recognize the field it is operating in. 


### Obstacle Challenge 🔴🟢:

<img src='' alt='map pic(obstacles)'>
Obstacle Challenge Field

To complete the second challenge, the robot must perform 3 full laps around the map with red and green "traffic signs" spread randomly across the canvas whilst driving in the correct lane around each one. In addition, the last block at the end of the second lap determines the direction that the robot continues in for its third lap. If that block was to be red, the robot has to continue in the opposite direction but, if that block was to be green, it continues as it is to then try to parallel park in the designated area at the end of lap 3.

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
    - Download and install RealVNC on your computer from [https://www.realvnc.com/en/connect/download/viewer/]
    - Open the Raspberry Pi terminal and run `sudo raspi-config`
    - Go to `Interface Options > VNC > Enable` 
    - Connect the laptop to the Pi via Ethernet cable
    - Set a static IP Address on the Pi so that the laptop can easily connect to it using `sudo nano /etc/dhcpcd.conf`
    - Save and reboot `sudo reboot`
    - Find the static IP on your computer, if it isn't set, enter `arp -a` into Command Prompt
    