import math
import random

# -------------------------------------------
# Objective function (WE MINIMIZE THIS)
# Example: f(x) = x^2  → minimum at x = 0
# -------------------------------------------
def cost(x):
    return x * x

# -------------------------------------------
# Small random step (neighbor)
# -------------------------------------------
def neighbor(x):
    return x + random.uniform(-1, 1)

# -------------------------------------------
# Simulated Annealing
# ΔE = cost(new) - cost(current)
# BETTER ⇒ ΔE < 0  (ALWAYS ACCEPT)
# WORSE  ⇒ accept with probability exp(-ΔE / T)
# -------------------------------------------
def simulated_annealing():

    current = random.uniform(-10, 10)
    current_cost = cost(current)

    T = 100.0                 # initial temperature
    T_min = 0.0001            # stopping temperature
    alpha = 0.99              # cooling factor

    print("Initial x =", current, "cost =", current_cost)

    while T > T_min:

        nxt = neighbor(current)
        nxt_cost = cost(nxt)

        deltaE = nxt_cost - current_cost

        # If delta < 0 → better → accept always
        if deltaE < 0:
            accept = True
        else:
            # Accept with probability exp(-ΔE/T)
            p = math.exp(-deltaE / T)
            accept = random.random() < p

        # Update state if accepted
        if accept:
            current = nxt
            current_cost = nxt_cost

        # Cool down temperature
        T = T * alpha

    print("Final solution:")
    print("x =", current, "cost =", current_cost)
    return current


# RUN
simulated_annealing()
