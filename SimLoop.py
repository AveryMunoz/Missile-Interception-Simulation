from PhysicsModel import air_density, forces, euler_integration
from Plot import trajectory_plot, forces_table
import numpy as np

# Defining missile constants (initial values that i could change later)
mass = 1500
g = 9.81
Cd = 0.3
missile_radius = 0.25
A = np.pi * missile_radius**2
H_t = 22500
max_thrust = 75000

# Time metrics
dt = 1
max_time = 1000

# Launch parameters
launch_angle = 60 * (np.pi / 180)
launch_velocity = 0

# Initial positions
position = np.array([0.01, 0.01])
velocity = np.array(
    [launch_velocity * np.cos(launch_angle), 
     launch_velocity * np.sin(launch_angle)]
)

# Create empty trajectory to store positions
trajectory = []
thrust_val = []
gravity_val = []
drag_val = []
altitude_val = []
time_val = []

t = 0

while position[1] >= 0 and t < max_time:
    altitude = position[1]
    F_total, F_thrust, F_drag, F_gravity, thrust_mag, drag_mag, gravity_mag = forces(mass, velocity, altitude, max_thrust, Cd, A, H_t, launch_angle, t)
    acceleration  = F_total / mass
    position, velocity = euler_integration(position, velocity, acceleration, dt)
    trajectory.append(position.copy()) # .copy() is used in order to store updating frames of position
    
    thrust_val.append(F_thrust)
    gravity_val.append(F_gravity)
    drag_val.append(F_drag)
    altitude_val.append(altitude)
    time_val.append(t)
    
    t += dt

trajectory = np.array(trajectory)
trajectory_plot(trajectory)
forces_table(altitude_val, thrust_val, drag_val, gravity_val, time_val)

