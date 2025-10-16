import numpy as np
import random
import math

def objective(state):
    """Return the negative number of attacking pairs (higher is better)."""
    n = len(state)
    conflicts = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1
    return -conflicts  # maximize this (minimize conflicts)

def random_neighbor(state):
    """Move one queen to a random row in its column."""
    n = len(state)
    neighbor = state.copy()
    col = random.randint(0, n - 1)
    new_row = random.randint(0, n - 1)
    while new_row == neighbor[col]:
        new_row = random.randint(0, n - 1)
    neighbor[col] = new_row
    return neighbor

def simulated_annealing(objective, n, max_iterations=10000, initial_temp=100.0, cooling_rate=0.99):
    """Simulated annealing search for N-Queens."""
    current = [random.randint(0, n - 1) for _ in range(n)]
    current_eval = objective(current)
    temperature = initial_temp

    for iteration in range(max_iterations):
        if -current_eval == 0:  # no conflicts
            break

        neighbor = random_neighbor(current)
        neighbor_eval = objective(neighbor)

        delta = neighbor_eval - current_eval
        # Accept new state if better or with some probability if worse
        if delta > 0 or random.random() < math.exp(delta / temperature):
            current, current_eval = neighbor, neighbor_eval

        temperature *= cooling_rate  # cool down

        if iteration % 100 == 0 or -current_eval == 0:
            print(f"Iter {iteration}: Conflicts = {-current_eval}, Temp = {temperature:.4f}")

    return current, current_eval

# Example: 8-Queens
n = 8
solution, value = simulated_annealing(objective, n)

print("\nFinal board (row positions for each column):", solution)
print("Final conflicts:", -value)

Output:

Iter 0: Conflicts = 7, Temp = 99.0000
Iter 100: Conflicts = 10, Temp = 36.2372
Iter 200: Conflicts = 9, Temp = 13.2640
Iter 300: Conflicts = 5, Temp = 4.8550
Iter 400: Conflicts = 3, Temp = 1.7771
Iter 500: Conflicts = 1, Temp = 0.6505
Iter 600: Conflicts = 4, Temp = 0.2381
Iter 700: Conflicts = 1, Temp = 0.0872
Iter 800: Conflicts = 1, Temp = 0.0319
Iter 900: Conflicts = 1, Temp = 0.0117
Iter 1000: Conflicts = 1, Temp = 0.0043
Iter 1100: Conflicts = 1, Temp = 0.0016
Iter 1200: Conflicts = 1, Temp = 0.0006
Iter 1300: Conflicts = 1, Temp = 0.0002
Iter 1400: Conflicts = 1, Temp = 0.0001
Iter 1500: Conflicts = 1, Temp = 0.0000
Iter 1600: Conflicts = 1, Temp = 0.0000
Iter 1700: Conflicts = 1, Temp = 0.0000
Iter 1711: Conflicts = 0, Temp = 0.0000

Final board (row positions for each column): [6, 1, 3, 0, 7, 4, 2, 5]
Final conflicts: 0
