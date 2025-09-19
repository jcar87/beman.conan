cmake_minimum_required(VERSION 3.15)

project(test_package LANGUAGES CXX)

find_package(beman.exemplar REQUIRED)

add_executable(test_package beman_exemplar.cpp)

target_link_libraries(test_package PRIVATE beman::exemplar)