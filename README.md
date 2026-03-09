# Monty Hall Problem — Monte Carlo Simulation

This repository contains a **Monte Carlo simulation of the Monty Hall problem**, implemented in **Python and Julia**, to empirically verify the theoretical probabilities of different strategies.

The goal is to compare the **stick** and **switch** strategies through large numbers of trials and observe how the experimental probabilities converge to the theoretical values.

---

## The Monty Hall Problem

The Monty Hall problem is a well-known puzzle in probability theory, named after **Monty Hall**, the host of the television game show *Let's Make a Deal*.

The setup is as follows:

* A contestant faces **three closed boxes**.
* **One box contains a prize**, while the other two are empty.
* The contestant selects one box.
* The host, who **knows where the prize is**, opens one of the remaining boxes that **does not contain the prize**.
* The contestant is then given a choice:

1. **Stick** with the original box
2. **Switch** to the other unopened box

The key question is:

> Does switching improve the probability of winning?

---

## Theoretical Result

The correct strategy is to **switch**.

| Strategy | Probability of Winning |
| -------- | ---------------------- |
| Stick    | 1/3                    |
| Switch   | 2/3                    |

Switching doubles the probability of winning because the initial choice has only a **1/3 chance** of being correct. When the host reveals an empty box, the remaining unopened box inherits the remaining probability mass.

---

## Monte Carlo Simulation

To verify this result experimentally, a Monte Carlo simulation is performed.

The simulation runs the game many times and records the win rates for both strategies.

As the number of trials increases:

* The **stick strategy converges to approximately 0.333**
* The **switch strategy converges to approximately 0.667**

This behavior demonstrates the **law of large numbers**.

---

## Running the Simulation

### Python

```bash
python monty_hall.py
```

### Julia

```bash
julia monty_hall.jl
```

Both implementations perform the same experiment and should produce similar results.

---

## Repository Structure

```
monty-hall-simulation
│
├── python
│   └── monty_hall.py
│
├── julia
│   └── monty_hall.jl
│
└── report
    └── Alpaslan_Kilic_220103067.pdf
```

---

## Author

Alpaslan Kılıç
