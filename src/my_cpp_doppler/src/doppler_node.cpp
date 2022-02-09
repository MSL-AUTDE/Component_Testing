#include <chrono>
#include <functional>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/int32.hpp"

using namespace std::chrono_literals;
using std::placeholders::_1;

/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class DopplerNode : public rclcpp::Node
{
  public:
    DopplerNode()
    : Node("doppler_node")
    {
      subscription_ = this->create_subscription<std_msgs::msg::Int32>(
      "integer", 10, std::bind(&DopplerNode::verdopple_integer, this, _1));

      publisher_ = this->create_publisher<std_msgs::msg::Int32>("doppelte_integer", 10);
    }

  private:

    void verdopple_integer(const std_msgs::msg::Int32::SharedPtr msg) const
    {
      RCLCPP_INFO(this->get_logger(), "I heard: %i", msg->data);

      auto message = std_msgs::msg::Int32();
      message.data = msg->data *2;

      RCLCPP_INFO(this->get_logger(), "Publishing: %i", message.data);
      publisher_->publish(message);
    }

    rclcpp::Publisher<std_msgs::msg::Int32>::SharedPtr publisher_;
    rclcpp::Subscription<std_msgs::msg::Int32>::SharedPtr subscription_;
};

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);
  rclcpp::spin(std::make_shared<DopplerNode>());
  rclcpp::shutdown();
  return 0;
}