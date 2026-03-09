# Monty Hall Simulation — Julia Code Explanation

This document explains the Julia implementation of the Monte Carlo simulation used to study the Monty Hall problem.

---

# 1. Importing Libraries

```julia
using Random, Statistics, Plots
gr()
```

Three Julia packages are used in this implementation.

## Random

The `Random` module provides tools for generating random numbers. In this simulation it is used to randomly generate:

* the contestant's initial box choice
* the actual prize location

Randomness is essential for performing a Monte Carlo experiment.

## Statistics

The `Statistics` module provides statistical functions such as:

```
mean()
```

This function is used to compute the empirical probability of winning.

## Plots

The `Plots` package is used to visualize the results of the simulation.

The command

```
gr()
```

selects the **GR backend**, which is one of the fastest plotting engines available in Julia.

---

# 2. Simulation Function

```julia
function simulate_monty_hall(N::Int, rng::AbstractRNG)::Tuple{Float64, Float64}
```

This function performs **N independent simulations of the Monty Hall game**.

## Function Arguments

| Argument | Description                 |
| -------- | --------------------------- |
| `N`      | number of simulation trials |
| `rng`    | random number generator     |

## Return Value

The function returns a tuple

```
(p_stick, p_switch)
```

where

* `p_stick` is the probability of winning when sticking with the original choice
* `p_switch` is the probability of winning when switching boxes

---

# 3. Generating the Initial Choice

```julia
X = rand(rng, 1:3, N)
```

This line generates **N random integers between 1 and 3**.

Each value represents the box initially selected by the contestant.

Example:

```
[1, 3, 2, 1, 1, 2]
```

Each entry corresponds to one simulated game.

---

# 4. Generating the Prize Location

```julia
Y = rand(rng, 1:3, N)
```

This line randomly assigns the location of the prize for each trial.

Example:

```
[2, 1, 2, 3, 1, 2]
```

For every simulation we now know:

* the contestant's initial choice
* the actual prize location

---

# 5. Determining the Switch Choice

```julia
Z = ifelse.(X .== Y, mod.(X, 3) .+ 1, Y)
```

This line computes the box that would be chosen **after switching**.

Two cases are possible.

### Case 1 — Initial choice was correct

```
X == Y
```

If the contestant initially selected the prize box, switching will lead to a losing box.

The expression

```
mod.(X,3) + 1
```

selects another box among the remaining ones.

### Case 2 — Initial choice was incorrect

If the initial choice is wrong, switching leads to the **prize box**.

Therefore

```
Z = Y
```

---

# 6. Computing Winning Probabilities

```julia
return mean(X .== Y), mean(Z .== Y)
```

These expressions compute the empirical probabilities.

```
mean(X == Y)
```

estimates

```
P(win | stick)
```

and

```
mean(Z == Y)
```

estimates

```
P(win | switch)
```

---

# 7. Running Simulations for Multiple Sample Sizes

```julia
function run_simulation(n_values::Vector{Int}; seed::Int=42)
```

This function runs the Monte Carlo experiment for multiple values of `N`.

Using different values of `N` allows us to observe how the estimated probabilities converge to the theoretical values.

---

# 8. Random Number Generator

```julia
rng = MersenneTwister(seed)
```

This creates a reproducible random number generator.

Using a fixed seed ensures that the simulation results can be reproduced.

---

# 9. Storing Results

```julia
p1_results = Float64[]
p2_results = Float64[]
```

Two arrays are created to store the estimated probabilities for

* the stick strategy
* the switch strategy

---

# 10. Running the Simulation Loop

```julia
for N in n_values
```

The simulation is repeated for different numbers of trials.

Typical values might include

```
10^3, 10^4, 10^5, 10^6
```

For each value the Monte Carlo simulation is executed.

---

```julia
p1, p2 = simulate_monty_hall(N, rng)
```

This performs the experiment and returns the estimated probabilities.

---

```julia
push!(p1_results, p1)
push!(p2_results, p2)
```

The results are stored in the arrays for later analysis.

---

# 11. Plotting the Results

```julia
function plot_results(n_values::Vector{Int}, p1::Vector{Float64}, p2::Vector{Float64})
```

This function visualizes the results of the simulation.

---

```julia
p = plot(n_values, p1,
    xscale = :log10,
    label = "Stick",
    color = :orange,
    lw = 2,
    xlabel = "Number of Trials (N)",
    ylabel = "Probability of Winning",
    title = "Monty Hall — Monte Carlo Simulation",
    grid = true,
    legend = :right,
    size = (800,450),
    framestyle = :box,
    margin = 5Plots.mm
)
```

This creates the base plot showing the probability of winning when sticking with the original choice.

The parameter `xscale = :log10` uses a logarithmic scale for the x-axis so that different orders of magnitude can be visualized clearly.

---

```julia
plot!(n_values, p2, label="Switch", color=:blue, lw=2)
```

This adds the switching strategy curve to the same plot.

---

```julia
savefig(p, "monty_hall.png")
```

The figure is saved as an image file.

---

# 12. Main Function

```julia
function main()
```

This function defines the experiment configuration and executes the simulation.

---

```julia
n_values = unique(round.(Int, 10 .^ range(3, 6, length=60)))
```

This generates simulation sizes between

```
10^3 and 10^6
```

The logarithmic spacing allows the convergence behavior to be observed clearly.

---

```julia
p1_results, p2_results = run_simulation(n_values)
```

Runs the simulations.

---

```julia
return plot_results(n_values, p1_results, p2_results)
```

Plots the results.

---

# 13. Executing the Program

```julia
main()
```

This line executes the entire simulation workflow.

---

# Summary

The program performs a Monte Carlo experiment of the Monty Hall game.

It demonstrates that

```
P(win | stick) ≈ 1/3
P(win | switch) ≈ 2/3
```

as predicted by probability theory.
