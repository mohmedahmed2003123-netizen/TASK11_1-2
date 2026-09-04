cmake_minimum_required(VERSION 3.8)
project(race_car_description)

find_package(ament_cmake REQUIRED)

# Install all necessary folders (urdf, launch, config) at once
install(
  DIRECTORY urdf launch config
  DESTINATION share/${PROJECT_NAME}
)

ament_package()