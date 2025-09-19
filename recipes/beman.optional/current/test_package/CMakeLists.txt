cmake_minimum_required(VERSION 3.15)

project(test_package LANGUAGES CXX)

find_package(BemanOptional REQUIRED)

add_executable(test_package beman_optional.cpp)
target_link_libraries(test_package PRIVATE Beman::Optional::beman_optional)