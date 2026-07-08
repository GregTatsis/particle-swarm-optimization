"""Particle Swarm Optimization example.

This script demonstrates Particle Swarm Optimization (PSO), a population-based
search algorithm inspired by the way a swarm explores a space together. Each
particle represents a candidate solution with three coordinates: x, y, and z.
During each iteration, particles update their velocities using their own best
known position and the swarm's best known position.

The objective is to minimize this quadratic function:

    f(x, y, z) = (x - 1)^2 + (y + 2)^2 + z^2

The global minimum is f(1, -2, 0) = 0, so a successful run should move the
swarm close to the point (1, -2, 0).
"""

import numpy as np


def objective_function(params):
    x, y, z = params[0], params[1], params[2]
    return (x - 1) ** 2 + (y + 2) ** 2 + z**2


bounds = np.array([[-10, -10, -10], [10, 10, 10]])
n_particles = 10
max_iter = 200
w = 0.5 #inertia weight
c1 = 0.8 #cognitive multiplier
c2 = 0.9 #social multiplier

particles = np.random.uniform(low=bounds[0], high=bounds[1], size=(n_particles, 3)) #position
velocities = np.zeros((n_particles, 3))
best_positions = particles.copy()
best_costs = np.array([objective_function(p) for p in particles])
global_best_position = particles[0].copy()
global_best_cost = best_costs[0]

for i in range(max_iter):
    r1 = np.random.rand(n_particles, 3)
    r2 = np.random.rand(n_particles, 3)

    cognitive = c1 * r1 * (best_positions - particles)
    social = c2 * r2 * (global_best_position - particles)

    velocities = w * velocities + cognitive + social #velocity update
    particles += velocities
    particles = np.clip(particles, bounds[0], bounds[1]) #make sure within bounds

    costs = np.array([objective_function(p) for p in particles])
    is_best = costs < best_costs
    best_positions[is_best] = particles[is_best]
    best_costs[is_best] = costs[is_best]

    global_best_index = np.argmin(best_costs)
    global_best_position = best_positions[global_best_index].copy()
    global_best_cost = best_costs[global_best_index]
    print(f"Iteration {i + 1}: Best Cost = {global_best_cost:.6f}")

print("Global Best Position:", global_best_position)
print("Global Best Cost:", global_best_cost)
