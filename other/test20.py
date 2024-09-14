from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='miivii_gmsl_camera',
            node_executable='miivii_gmsl_camera_node',
            node_name='miivii_gmsl_camera_node',
            output='screen',
            parameters=[
                {'sync_freq': 30},
                {'video0.active': True},
                {'video1.active': True},
                ]
        ),
        Node(
            package='rviz2',
            node_executable='rviz2',
            node_name='rviz2',
            output='screen',
            arguments=['-d', '/home/camera/install/miivii_gmsl_camera/share/miivii_gmsl_camera/config/multi.rviz']
        ),
    ])
