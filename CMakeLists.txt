cmake_minimum_required(VERSION 2.8)

project(learnEigen)

set(CMAKE_BUILD_TYPE "RELEASE")

set(CMAKE_CXX_FLAGS "-O3")

include_directories("/usr/include/eigen3")

add_executable(test_eigen test_eigen.cpp)