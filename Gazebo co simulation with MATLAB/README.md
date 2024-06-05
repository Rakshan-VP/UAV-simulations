# Gazebo Co-simulation with MATLAB
This page shows how to set up a synchronized simulation between Simulink™ and Gazebo to send commands and receive data from Gazebo.
![gazebo_co](https://github.com/tech-lover-1510/UAV-simulations/assets/136898779/8511ec4b-b4c5-4c31-9dd6-ea1d1136c22e)

## Installing Gazebo plugin
- Open Matlab and run the command:
  ```matlab
  packageGazeboPlugin
  ```
  It will create **GazeboPlugin.zip** file.
  
- Copy the **GazeboPlugin.zip** to your Linux machine. Unzip the package on your Linux platform, for this example we unpack to **/home/user/src/GazeboPlugin**.
  ```matlab
  cd /home/user/src/GazeboPlugin
  ```
- Install plugin
  ```matlab  
  mkdir build
  cd build
  cmake ..
  make
  ```

## Running files in Gazebo
- Add the **world** file in the examples to the directory **/home/user/src/GazeboPlugin/world**.
- Now go to export directory and run the following commands:
  ```matlab
  cd /home/user/src/GazeboPlugin/export
  export SVGA_VGPU10=0
  ```
- Now run the **world** file using the command:
  ```matlab
  gazebo ../world/quadcopter.world --verbose
  ```
  Instead of **quadcopter.world** put your world file name.
  
## Simulink model
 Open the Simulink model in Matlab and run it to control the Gazebo model and get data from it.

##
For more details, [click here](https://in.mathworks.com/help/robotics/ug/perform-co-simulation-between-simulink-and-gazebo.html#PerformCoSimulationBetweenSimulinkAndGazeboExample-2)
