# **Object Tracking with Sensor Fusion-based Kalman Filter**

## Objective
Utilize sensor data from both LIDAR and RADAR measurements for object (e.g. pedestrian, vehicles, or other moving objects) 
tracking with the Kalman Filter.

## Code & Files
### 1. Dependencies & environment

* cmake >= 3.5
 * All OSes: [click here for installation instructions](https://cmake.org/install/)
* make >= 4.1
  * Linux: make is installed by default on most Linux distros
  * Mac: [install Xcode command line tools to get make](https://developer.apple.com/xcode/features/)
  * Windows: [Click here for installation instructions](http://gnuwin32.sourceforge.net/packages/make.htm)
* gcc/g++ >= 5.4
  * Linux: gcc / g++ is installed by default on most Linux distros
  * Mac: same deal as make - [install Xcode command line tools]((https://developer.apple.com/xcode/features/)
  * Windows: recommend using [MinGW](http://www.mingw.org/)
* [Eigen library](src/Eigen)


### 2. My project files

(Note: the hyperlinks **only** works if you are on the homepage of this GitHub reop,
and if you are viewing it in "github.io" you can be redirected by clicking the **View the Project on GitHub** on the top)

* [CMakeLists.txt](CMakeLists.txt) is the cmake file.

* [data](data) folder contains test lidar and radar measurements.

* [Docs](Docs) folder contains docments which describe the data.

* [src](src) folder contains the source code.


### 3. Code Style

* [Google's C++ style guide](https://google.github.io/styleguide/cppguide.html).


### 4. How to run the code

1. Clone this repo.
2. Make a build directory: `mkdir build && cd build`
3. Compile: `cmake .. && make` 
   * On windows, you may need to run: `cmake .. -G "Unix Makefiles" && make`
4. Run it by the following commands: 
   * `./KF  ../data/obj_pose-laser-radar-synthetic-input.txt ./output.txt`





[//]: # (Image References)
[image1]: ./images/ctrv.jpg
[image2]: ./images/ukf_roadmap.jpg
[image3]: ./images/ukf.jpg
