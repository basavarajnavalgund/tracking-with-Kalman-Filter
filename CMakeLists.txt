project(KF)

cmake_minimum_required (VERSION 3.5)

add_definitions(-std=c++0x)

set(sources
    src/FusionEKF.cpp
    src/kalman_filter.cpp
    src/main.cpp
    src/tools.cpp)

add_executable(KF ${sources})
