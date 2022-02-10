# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


class Plus2Node(Node):

    def __init__(self):
        super().__init__('plus_2_node')
        self.publisher_ = self.create_publisher(Int32, 'plus_2', 10)

        self.subscription = self.create_subscription(
            Int32,
            'doppelte_integer',
            self.plus2_callback,
            10)
        self.subscription

    def plus2_callback(self,msg):
        self.get_logger().info('Received: "%i"' % msg.data)
        message = Int32()
        message.data = msg.data + 2
        self.publisher_.publish(message)
        self.get_logger().info('Publishing: "%i"' % message.data)


def main(args=None):
    rclpy.init(args=args)

    plus_2_node = Plus2Node()

    rclpy.spin(plus_2_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    plus_2_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
