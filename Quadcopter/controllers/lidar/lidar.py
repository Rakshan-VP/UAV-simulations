from controller import Robot, Lidar, Motor
import numpy as np
import matplotlib.pyplot as plt

# Init
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Devices
lidar = robot.getDevice("lidar")
motor = robot.getDevice("lidar motor")

lidar.enable(timestep)
lidar.enablePointCloud()

# Rotate continuously
motor.setPosition(float('inf'))  # infinite rotation
motor.setVelocity(2.0)           # radians/sec (adjust as needed)

# LiDAR specs
resolution = lidar.getHorizontalResolution()
fov = lidar.getFov()
angle_step = fov / resolution

# Plot init
plt.ion()
fig, ax = plt.subplots()
sc = ax.scatter([], [])
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("LIDAR Obstacle Map")
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.grid(True)

while robot.step(timestep) != -1:
    ranges = lidar.getRangeImage()
    
    x_vals = []
    y_vals = []

    for i, r in enumerate(ranges):
        if r != float('inf') and r > 0.01:
            angle = -fov / 2 + i * angle_step
            x = r * np.cos(angle)
            y = r * np.sin(angle)
            x_vals.append(x)
            y_vals.append(y)
    
    # Update plot
    sc.set_offsets(np.c_[x_vals, y_vals])
    plt.draw()
    plt.pause(0.001)
