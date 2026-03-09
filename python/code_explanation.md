# Monty Hall Simulation — Code Explanation

This document explains the Python implementation of the Monty Hall Monte Carlo simulation step by step.

---

# 1. Importing Libraries

```python
import numpy as np
import matplotlib.pyplot as plt
```

## NumPy

NumPy is a scientific computing library for Python. It provides fast array operations and random number generation.

In this project it is used for:

* generating random choices
* vectorized computations
* computing averages

## Matplotlib

Matplotlib is a plotting library used to visualize the results of the simulation.

In this project it is used to:

* plot the estimated probabilities
* compare them with the theoretical values

---

# 2. Monty Hall Simulation Function

```python
def simulate_monty_hall(N: int, rng: np.random.Generator) -> tuple[float, float]:
```

This function simulates the Monty Hall game **N times**.

## Parameters

| Parameter | Description                        |
| --------- | ---------------------------------- |
| N         | number of trials in the simulation |
| rng       | random number generator            |

## Return Values

The function returns two values:

```
(p_stick, p_switch)
```

where

* `p_stick` is the probability of winning when **sticking** with the original choice
* `p_switch` is the probability of winning when **switching**

---

# 3. Generating the Initial Choice

```python
initial_choice = rng.integers(1, 4, N)
```

This line generates **N random integers between 1 and 3**.

Each value represents the box initially chosen by the contestant.

Example:

```
[1, 3, 2, 1, 1, 2]
```

Each number corresponds to one of the three boxes.

---

# 4. Generating the Prize Location

```python
prize = rng.integers(1, 4, N)
```

This line randomly assigns the prize location for each trial.

Example:

```
[2, 1, 2, 3, 1, 2]
```

For every simulation run we now have

* the contestant's initial choice
* the actual prize location

---

# 5. Determining the Switch Choice

```python
switch_choice = np.where(initial_choice == prize, (initial_choice % 3) + 1, prize)
```

This line computes the box that would be chosen **after switching**.

Two cases exist.

## Case 1 — Initial choice was correct

```
initial_choice == prize
```

If the contestant initially selected the prize box, switching will lead to a losing box.

The expression

```
(initial_choice % 3) + 1
```

simply selects another box among the remaining two.

## Case 2 — Initial choice was incorrect

If the initial choice is wrong, switching must lead to the **prize box**.

Therefore

```
switch_choice = prize
```

---

# 6. Computing Winning Probabilities

```python
p_stick = np.mean(initial_choice == prize)
```

This computes the fraction of trials in which the initial choice was correct.

Mathematically this estimates

```
P(win | stick)
```

---

```python
p_switch = np.mean(switch_choice == prize)
```

This computes the fraction of trials where switching leads to the prize.

Mathematically this estimates

```
P(win | switch)
```

---

# 7. Returning the Results

```python
return p_stick, p_switch
```

The function returns the estimated probabilities of winning for both strategies.

---

# 8. Running the Simulation for Different Sample Sizes

```python
def run_simulation(n_values: np.ndarray, seed: int = 42) -> tuple[list, list]:
```

This function runs the Monty Hall simulation for **multiple values of N**.

Using different sample sizes allows us to observe the **convergence of probabilities**.

---

# 9. Creating the Random Generator

```python
rng = np.random.default_rng(seed)
```

This creates a reproducible random number generator.

The seed ensures that the results are **repeatable**.

---

# 10. Storing Results

```python
p1_results, p2_results = [], []
```

Two lists are created to store the estimated probabilities for

* the stick strategy
* the switch strategy

---

# 11. Running the Simulation Loop

```python
for N in n_values:
```

The simulation is repeated for different numbers of trials.

Example values might include

```
1000
10000
100000
1000000
```

For each value of N the simulation function is executed.

---

```python
p1, p2 = simulate_monty_hall(N, rng)
```

This runs the Monte Carlo experiment.

---

```python
p1_results.append(p1)
p2_results.append(p2)
```

The estimated probabilities are stored for later plotting.

---

# 12. Plotting the Results

```python
def plot_results(n_values: np.ndarray, p1: list, p2: list) -> None:
```

This function is responsible for **visualizing the results of the Monte Carlo simulation**.

### Function Arguments

| Argument   | Meaning                                                            |
| ---------- | ------------------------------------------------------------------ |
| `n_values` | Array containing the number of trials used in each simulation      |
| `p1`       | Estimated winning probabilities when using the **stick strategy**  |
| `p2`       | Estimated winning probabilities when using the **switch strategy** |

The purpose of this function is to show **how the empirical probabilities converge toward the theoretical probabilities (1/3 and 2/3)** as the number of trials increases.

---

### Creating the Figure

```python
fig, ax = plt.subplots(figsize=(8,4))
```

This line creates a **figure and axis object**.

* `fig` represents the entire figure window
* `ax` represents the coordinate system where the graph will be drawn

The parameter `figsize=(8,4)` sets the width and height of the plot in inches.

This step is necessary because Matplotlib organizes plots using the **figure–axis hierarchy**.

---

### Plotting the Simulation Results

```python
ax.semilogx(n_values, p1, label="Stick")
ax.semilogx(n_values, p2, label="Switch")
```

These two lines draw the main curves of the simulation.

`semilogx` means that the **x-axis is plotted on a logarithmic scale**, while the y-axis remains linear.

This is important because the number of trials ranges from

```
10^3 to 10^6
```

Using a logarithmic axis allows us to visualize **multiple orders of magnitude clearly**.

The plotted curves represent:

| Curve  | Meaning                                             |
| ------ | --------------------------------------------------- |
| Stick  | Estimated probability of winning when not switching |
| Switch | Estimated probability of winning when switching     |

Each point corresponds to the probability estimate obtained after running a simulation with a specific number of trials.

---

### Plotting Theoretical Reference Lines

```python
ax.axhline(1/3)
ax.axhline(2/3)
```

These lines draw **horizontal reference lines** representing the theoretical probabilities predicted by probability theory.

| Value | Interpretation                                    |
| ----- | ------------------------------------------------- |
| 1/3   | Theoretical probability of winning when sticking  |
| 2/3   | Theoretical probability of winning when switching |

These lines allow us to visually verify that the simulated probabilities converge to the expected theoretical values.

---

# 13. Labels and Title

```python
ax.set_xlabel("Number of Trials (N)")
ax.set_ylabel("Probability of Winning")
ax.set_title("Monty Hall Monte Carlo Simulation")
```

These commands label the axes and title of the graph.

---

# 14. Displaying the Plot

```python
plt.savefig("monty_hall.png")
plt.show()
```

The figure is

* saved as an image file
* displayed on screen

---

# 15. Main Function

```python
def main():
```

This function defines the experiment configuration.

---

```python
N_values = np.unique(np.round(np.logspace(3,6,60)).astype(int))
```

This generates trial sizes between

```
10^3 and 10^6
```

The logarithmic spacing allows the convergence behavior to be visualized.

---

```python
p1_results, p2_results = run_simulation(N_values)
```

Runs the simulations.

---

```python
plot_results(N_values, p1_results, p2_results)
```

Plots the results.

---

# 16. Script Entry Point

```python
if __name__ == "__main__":
    main()
```

This ensures that the simulation runs when the file is executed as a script.

---

# Summary

The program performs a Monte Carlo experiment of the Monty Hall game.

It demonstrates that

```
P(win | stick) ≈ 1/3
P(win | switch) ≈ 2/3
```

as predicted by probability theory.

