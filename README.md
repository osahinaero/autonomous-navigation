# Autonomous Navigation

## Overview
This project simulates an autonomous agent navigating a 2D grid with obstacles to reach a target location.

It explores three approaches:
1. Greedy algorithm
2. Greedy algorithm with memory
3. A* pathfinding

---

At each step, the agent evaluates possible moves and selects the best option based on:
- grid boundaries
- obstacle avoidance
- distance to the target

---

##  Iterations

### Iteration 1: Greedy
- Moves toward the target using shortest immediate distance
- Fast but can get stuck in loops

### Iteration 2: Greedy + Memory
- Tracks visited positions
- Avoids revisiting nodes
- Reduces looping

### Iteration 3: A* Pathfinding
- Uses cost + heuristic (f = g + h)
- Finds optimal path
- Avoids loops and dead ends

---

## How to Run

```bash
python "Iteration 1_Greedy Algorithm.py"
python "Iteration 2_Greedy AlgorithmwithMemory.py"
python "Iteration 3_A Pathfinding.py"
