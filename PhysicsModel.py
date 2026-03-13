import numpy as np

def air_density(altitude):
    rho_0 = 1.225
    H = 8500
    rho = rho_0 * (np.exp((-altitude)/H))
    return rho

def forces(mass, velocity, altitude, max_thrust, Cd, A, H_t):
    rho = air_density(altitude)
    
    g = 9.81
    Cd = 0.3
    missile_radius = 0.25
    A = np.pi * missile_radius**2
    H_t = 17500
    
    F_gravity  = np.array([0.0, -mass * 9.81])
    
    velocity_mag = np.linalg.norm(velocity)
    drag_mag = 0.5 * rho * velocity_mag**2 * Cd * A
    F_drag = -drag_mag * (velocity / velocity_mag)
    
    thrust_mag = max_thrust * np.exp(-altitude / H_t)
    F_thrust = thrust_mag * (velocity / velocity_mag)
    
    tot_force = F_thrust + F_drag + F_gravity
    
    return tot_force
    
    
def euler_integration(position, velocity, acceleration, dt):
    new_velocity = velocity + (acceleration * dt)
    new_position = position + (new_velocity * dt)
    return new_position, new_velocity
    
    