import numpy as np

# Simulation parameters
num_particles = 10
dt = 0.01  # Time step
g = np.array([0, -9.81])  # Gravity

# Particle properties
positions = np.random.rand(num_particles, 2) * 10  # Random initial positions
velocities = np.zeros((num_particles, 2))  # Initial velocities
masses = np.ones(num_particles)  # Masses of particles

def update_positions(positions, velocities, dt):
    return positions + velocities * dt

def update_velocities(velocities, dt):
    return velocities + g * dt

import matplotlib.pyplot as plt

def plot_particles(positions):
    plt.clf()
    plt.scatter(positions[:, 0], positions[:, 1])
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.pause(0.01)

plt.ion()  # Turn on interactive mode for live updates

for _ in range(1000):  # Run the simulation for 1000 steps
    positions = update_positions(positions, velocities, dt)
    velocities = update_velocities(velocities, dt)
    plot_particles(positions)
    
plt.ioff()  # Turn off interactive mode
plt.show()

def handle_collisions(positions, velocities):
    for i in range(len(positions)):
        if positions[i, 0] <= 0 or positions[i, 0] >= 10:
            velocities[i, 0] *= -1  # Reverse velocity on X-axis collision
        if positions[i, 1] <= 0 or positions[i, 1] >= 10:
            velocities[i, 1] *= -1  # Reverse velocity on Y-axis collision

for _ in range(1000):
    positions = update_positions(positions, velocities, dt)
    velocities = update_velocities(velocities, dt)
    handle_collisions(positions, velocities)
    plot_particles(positions)

