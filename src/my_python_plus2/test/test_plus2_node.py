import unittest

from launch import LaunchContext
from launch import LaunchDescription
from launch import LaunchService
from launch_ros.actions import Node
from launch.actions import Shutdown
from launch.substitutions import EnvironmentVariable

import launch_ros.actions.node
from launch_ros.descriptions import Parameter
from launch_ros.descriptions import ParameterValue

import pytest
import yaml
        
def test_plus2():
    plus2_node = Node(
        package = 'my_python_plus2',
        name = 'plus2_node',
        executable = 'plus2',
        output='screen',
    )


    ld = LaunchDescription()
    ld.add_action(plus2_node)

    ls = LaunchService(debug=True)
    ls.include_launch_description(ld)
    ret = ls.run()
    assert 0 == ret
        
if __name__ == '__main__':     
    test_plus2()