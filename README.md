# sensors_demos_gazebo

Installation:

1. In your workspace `src` directory: `git clone https://github.com/Jakubach/sensors_demos_gazebo.git`
2. `sudo rosdep init` 
3. `rosdep update`
4. `rosdep install --from-paths src -y --ignore-src --rosdistro humble`
5. `colcon build`

Running:
1. In your workspace main directory: `source install/setup.bash`
2. Running with `launch` files:

Hokuyo sensor:

*  `ros2 launch sensors_demos_gazebo hokuyo_launch.py`

Imu sensor:

* `ros2 launch sensors_demos_gazebo imu_launch.py`

Kinect sensor:

* `ros2 launch sensors_demos_gazebo kinect_launch.py`
