#Projectile motion simulation using matplotlib

import matplotlib.pyplot as plt
import numpy as np 

def projectile_motion():
    g = 9.81
    try:
        initial_velocity = float(input("Enter the initial velocity (m/s): "))
    except ValueError:
        print("Invalid input. Please enter a numeric value for initial velocity.")
    else:
        try:
            angle = float(input("Enter the launch angle (degrees): "))
        except ValueError:
            print("Invalid input. Please enter a numeric value for the launch angle.")
        else:
            time = (2*initial_velocity*np.sin(np.radians(angle)))/g
            t = np.linspace(0, time, 100) 
            theta = np.radians(angle)
            x = initial_velocity*np.cos(theta)*t
            y = initial_velocity*np.sin(theta)*t - 0.5*g*t**2
            plt.figure(figsize=(10, 8))
            plt.ylim(bottom=0)
            plt.axis('equal')
            plt.plot(x, y, label='Trajectory')
            plt.legend()
            plt.grid(True, alpha=0.3)
            plt.title('Projectile Motion')
            plt.xlabel('Distance (m)')
            plt.ylabel('Height (m)')
            plt.show()

projectile_motion()