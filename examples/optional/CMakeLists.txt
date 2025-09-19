cmake_minimum_required(VERSION 3.27)

project(BemanExample LANGUAGES CXX)

find_package(BemanOptional REQUIRED)

add_executable(example src/example.cpp)

target_link_libraries(example PRIVATE Beman::Optional::beman_optional)
