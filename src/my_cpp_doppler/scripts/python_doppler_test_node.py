import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32


def CompareIntMsg(msg_input, msg_output) -> bool:
    return msg_input.data == msg_output.data


class PythonDopplerTestNode(Node):

    def __init__(self):
        super().__init__('doppler_test_node')
        self.publisher_ = self.create_publisher(Int32, 'integer', 10)

        self.subscription = self.create_subscription(
            Int32,
            'doppelte_integer',
            self.doppler_test_callback,
            10)
        self.subscription

        self.index = 0
        self.List_Tests = [(1, 2), (3, 6), (5, 10)]
        message = Int32()
        message.data = self.List_Tests[self.index][0]
        self.publisher_.publish(message)

    def doppler_test_callback(self, msg):
        self.get_logger().info('Received: "%i"' % msg.data)
        message_test = Int32()
        message_test.data = self.List_Tests[self.index][1]
        self.get_logger().info('Output is right: "%r"' %
                               CompareIntMsg(message_test, msg))
        self.index += 1

        if self.index < len(self.List_Tests):
             message = Int32()
             message.data = self.List_Tests[self.index][0]
             self.publisher_.publish(message)


def main(args=None):
    rclpy.init(args=args)

    doppler_test_node = PythonDopplerTestNode()

    rclpy.spin(doppler_test_node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    doppler_test_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
