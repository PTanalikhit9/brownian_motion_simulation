import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
D = 1 # Diffusion coefficient
dt = 0.01 # Time step
t_max = 10 # Total simulation time
n_steps = int(t_max / dt) # Number of time steps

# Initialize particle position and velocity arrays
x = np.zeros(n_steps)
y = np.zeros(n_steps)

# Simulate Brownian motion
for i in range(1, n_steps):
    x[i] = x[i-1] + np.sqrt(2 * D * dt) * np.random.normal()
    y[i] = y[i-1] + np.sqrt(2 * D * dt) * np.random.normal()
