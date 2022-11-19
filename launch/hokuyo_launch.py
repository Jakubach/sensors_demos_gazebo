import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import xacro


def generate_launch_description():

  use_sim_time = LaunchConfiguration('use_sim_time', default='false')
  xacro_file_name = 'hokuyo.urdf.xacro'

  xacro_file = os.path.join(get_package_share_directory('sensors_demos_gazebo'), xacro_file_name)
  assert os.path.exists(xacro_file), "The " + xacro_file_name + " doesnt exist in "+str(xacro_file)

  robot_description_config = xacro.process_file(xacro_file)
  robot_desc = robot_description_config.toxml()
  
  return LaunchDescription([
  
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),

        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),
            
	Node(package="robot_state_publisher",executable="robot_state_publisher",name="robot_state_publisher",parameters=[{"robot_description": robot_desc}],output="screen"),		
	Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            name='joint_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time}]
            ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='urdf_spawner',
            output='screen',
            arguments=["-topic", "/robot_description", "-entity", xacro_file_name])
  ])
  

