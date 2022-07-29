import os

import launch
import launch.conditions
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
import launch.conditions
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description():

    avt_341_package_dir = get_package_share_directory('avt_341')
    urdf = os.path.join(avt_341_package_dir, 'config', 'avt_bot.urdf')
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()
    waypoints_file = os.path.join(
        avt_341_package_dir,
        'config',
        'waypoints-loop-unreal-01.yaml'
    )
    avt_341_dir = get_package_share_directory('avt_341')
    base_launch = launch.actions.IncludeLaunchDescription(
        PythonLaunchDescriptionSource(os.path.join(avt_341_dir, 'launch', 'base.launch.py')),
        launch_arguments={'waypoints_file': waypoints_file,
                          'robot_description': robot_desc,
                          'use_sim_time': 'False',
                          'goal_dist': '7.0',
                          'path_look_ahead': '40.0',
                          'stitch_lidar_points': 'False',
                          'use_registered': 'False',
                          'slope_threshold': '2.5',
                          'vehicle_width': '5.0',
                          'grid_dilate': 'True',
                          'grid_dilate_y': '3.0',
                          'w_s': '1.0',
                          'steering_coefficient': '2.5',
                          'vehicle_max_steer_angle_degrees': '38.7',
                          'vehicle_wheelbase': '3.3',
                          'cull_lidar': 'True',
                          'cull_lidar_dist': '70.0'}.items()
    )

    launch_description = LaunchDescription([
        base_launch
    ])

    return launch_description