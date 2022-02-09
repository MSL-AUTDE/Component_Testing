cmake_minimum_required(VERSION 3.5)
project(my_cpp_doppler)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(launch_testing_ament_cmake)
add_launch_test(test/doppler_launch_test.py)

add_executable(doppler src/doppler_node.cpp)
ament_target_dependencies(doppler rclcpp std_msgs)

install(TARGETS
  doppler
  DESTINATION lib/${PROJECT_NAME})

ament_package()
