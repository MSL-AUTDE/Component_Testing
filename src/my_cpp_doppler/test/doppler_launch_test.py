import launch
import launch.actions
from launch_ros.actions import Node

import launch_testing
import launch_testing.actions
import launch_testing.markers
from launch_testing.asserts import assertSequentialStdout

import unittest
import pytest


# @pytest.mark.launch_test
@launch_testing.markers.keep_alive
def generate_test_description():
    return launch.LaunchDescription([
        #Node(
        #    package='my_cpp_doppler',
        #    namespace='doppler',
        #    executable='doppler',
        #    name='doppler'
        #),
        # Launch a process to test
        launch.actions.ExecuteProcess(
            cmd=['echo', 'hello_world'],
            shell=True
        ),
        launch_testing.actions.ReadyToTest(),
    ])


# This is our test fixture. Each method is a test case.
# These run alongside the processes specified in generate_test_description()
class TestHelloWorldProcess(unittest.TestCase):

    def test_read_stdout(self, proc_output):
        """Check if 'hello_world' was found in the stdout."""
        # 'proc_output' is an object added automatically by the launch_testing framework.
        # It captures the outputs of the processes launched in generate_test_description()
        # Refer to the documentation for further details.
        proc_output.assertWaitFor('hello_world', timeout=10, stream='stdout')


@launch_testing.post_shutdown_test()
class TestProcessOutput(unittest.TestCase):

    def test_exit_code(self, proc_info):
        # Check that all processes in the launch (in this case, there's just one) exit
        # with code 0
        launch_testing.asserts.assertExitCodes(proc_info)
        
    