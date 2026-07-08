# Particle Swarm Optimization Demo

This repository contains a small Python implementation of Particle Swarm
Optimization (PSO).

The script minimizes the quadratic objective function:

```text
f(x, y, z) = (x - 1)^2 + (y + 2)^2 + z^2
```

The global minimum is:

```text
f(1, -2, 0) = 0
```

PSO starts with a swarm of random particles and repeatedly updates each
particle's velocity and position based on:

- its own best known position
- the swarm's global best known position
- random exploration factors

## Requirements

```bash
pip install numpy
```

## Run

```bash
python pso_quadratic_minimizer.py
```

The program prints the best cost found at each iteration and the final best
position discovered by the swarm.
