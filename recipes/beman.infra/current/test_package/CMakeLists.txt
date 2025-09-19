cmake_minimum_required(VERSION 3.15)


project(test_package LANGUAGES CXX)

find_package(beman-install-library REQUIRED)

if(NOT COMMAND beman_install_library)
    message(FATAL_ERROR "beman_install_library not found. Something is wrong with the beman.cmake package")
endif()
