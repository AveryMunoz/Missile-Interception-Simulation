import numpy as np

def air_density(altitude):
    rho_0 = 1.225
    H = 8500
    rho = rho_0 * (np.exp((-altitude)/H))
    return rho

def forces(mass, velocity, altitude, max_thrust, Cd, A, H_t, launch_angle, t):
    rho = air_density(altitude)
    vector_direction = np.array([
            np.cos(launch_angle),
            np.sin(launch_angle)
        ])
    
    F_gravity  = np.array([0.0, -mass * 9.81])
    gravity_mag = np.linalg.norm(F_gravity)
    
    velocity_mag = np.linalg.norm(velocity)
    
    if velocity_mag == 0:
        drag_mag = 0.5 * rho * velocity_mag**2 * Cd * A
        F_drag = -drag_mag * vector_direction
    else:
        drag_mag = 0.5 * rho * velocity_mag**2 * Cd * A
        F_drag = -drag_mag * (velocity / velocity_mag)
    
    if t > 120:  
        thrust_mag = 0.0
        F_thrust = thrust_mag * vector_direction
    else:
        thrust_mag = max_thrust * np.exp(-altitude / H_t)
        F_thrust = thrust_mag * vector_direction
    
    tot_force = F_thrust + F_drag + F_gravity
    
    return tot_force, F_thrust, F_drag, F_gravity, thrust_mag, drag_mag, gravity_mag
    
    
def euler_integration(position, velocity, acceleration, dt):
    new_velocity = velocity + (acceleration * dt)
    new_position = position + (new_velocity * dt)
    return new_position, new_velocity
    
    