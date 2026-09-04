# ROS 2 Race Car Tasks (Jazzy + Gazebo Harmonic)

This repository contains the implementation of **Task 11.1** (Robot Simulation) and **Task 11.2** (Camera‑to‑Base Transformation) for the Electrical Team.

---

## 📁 Repository Structure

ros2_race_car_tasks/
├── config/
│   └── rviz_config.rviz         # RViz configuration file
├── launch/
│   └── race_car.launch.py       # Launch file for Gazebo simulation
├── urdf/
│   └── race_car.xacro           # Robot model (XACRO)
├── CMakeLists.txt               # ROS 2 build configuration
├── package.xml                  # ROS 2 package manifest
├── task11_2.py                  # Camera‑to‑base transformation script
└── README.md                    # This file


---

## 🛠️ Dependencies

Install the required ROS 2 packages (Jazzy):

bash
sudo apt update
sudo apt install ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-bridge \
                 ros-jazzy-xacro ros-jazzy-joint-state-publisher-gui

---

🏎️ Task 11.1 – Robot Simulation

Run the Simulation

1. Copy the package into your ROS workspace:

bash
cp -r ~/path/to/this/repo ~/ros2_ws/src/race_car_description

2. Build the package:

bash
cd ~/ros2_ws
colcon build --packages-select race_car_description
source install/setup.bash

3. Launch the simulation:

bash
ros2 launch race_car_description race_car.launch.py

4. Test movement (in a new terminal):

bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5}, angular: {z: 0.2}}"

The car should move forward and turn.

Note: If the Gazebo window appears black, this is a graphics driver issue – the simulation is still running correctly.

---

Task 11.2 – Camera‑to‑Base Transformation

Overview

The script transforms 3D obstacle points from the camera frame (camera_link) to the car's centre frame (base_link) using:

· Rotation around the Y‑axis (pitch -15°).
· Translation by the camera offset (tx, ty, tz) = (0.5, 0.0, 0.2).

Input Points (camera frame)

python
points = [
    [2.0, 0.0, -0.2],
    [3.5, 1.0, -0.3],
    [1.5, -0.8, -0.1]
]

Run the Script

bash
python3 task11_2.py

Expected Output

Transformed Obstacles (Base Frame):
Obstacle 1: [2.48, 0.00, 0.52]
Obstacle 2: [3.96, 1.00, 0.82]
Obstacle 3: [1.97, -0.80, 0.29]
`

The script uses only math – no ROS 2 required.

