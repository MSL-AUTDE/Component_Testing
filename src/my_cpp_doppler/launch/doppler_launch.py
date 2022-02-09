from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_cpp_doppler',
            namespace='doppler',
            executable='doppler',
            name='doppler'
        ),
    ])
