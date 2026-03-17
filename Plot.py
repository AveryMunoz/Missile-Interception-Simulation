import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def trajectory_plot(trajectory):
    x = trajectory[:, 0] / 1000
    y = trajectory[:, 1] / 1000
    
    plt.title("Sim Test Run")
    plt.xlabel("Horizontal Distance (km)")
    plt.ylabel("Altitude (km)")
    plt.plot(x, y, color = "red")
    plt.show()

def forces_table(altitude_val, thrust_val, drag_val, gravity_val, time_val):
    forces_data = {
        "Time (s)": time_val,
        "Altitude (m)": altitude_val,
        "Thrust (N)": thrust_val,
        "Drag (N)": drag_val,
        "Gravity (N)": gravity_val
    }
    
    df = pd.DataFrame(forces_data)
    df.to_csv("simulation_output1.csv", index=False)
    