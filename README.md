# Monty Hall Problem — Monte Carlo Simulation

This repository studies the **Monty Hall problem** from a probabilistic and computational perspective. The objective is to compare the **theoretical solution derived from probability theory** with **empirical results obtained through Monte Carlo simulation**.

The simulation is implemented in **Python and Julia** in order to verify that the long‑run frequencies converge to the theoretical probabilities predicted by the mathematical model.

---

# The Monty Hall Problem

The Monty Hall problem is a classical example in probability theory that illustrates how **conditional probability and information revealed during a process can dramatically change optimal decision strategies**.

The problem is named after **Monty Hall**, host of the television game show *Let's Make a Deal*.

The game proceeds as follows:

1. A contestant faces **three closed boxes**.
2. Exactly **one box contains a prize**, while the other two contain nothing.
3. The contestant selects one box.
4. The host, who **knows the location of the prize**, opens one of the remaining boxes that **does not contain the prize**.
5. The contestant is then offered a choice:

* **Stick** with the original box
* **Switch** to the other unopened box

The central question is:

> Does switching improve the probability of winning?

Many people intuitively believe that after one empty box is opened the remaining two boxes should each have probability 1/2. However, this reasoning ignores the **information contained in the host's action**.

---

# Theoretical Result

The optimal strategy is to **switch boxes**.

| Strategy | Probability of Winning |
| -------- | ---------------------- |
| Stick    | 1/3                    |
| Switch   | 2/3                    |

Thus, switching **doubles the probability of winning**.

---

# Probabilistic Analysis

Let

* (W_i) denote the event that the prize is behind box *i*
* (H_j) denote the event that the host opens box *j*

Assume the contestant initially selects **Box 1**.

The prior probabilities are

[
P(W_1) = P(W_2) = P(W_3) = \frac{1}{3}
]

The host's strategy is constrained by the rules of the game:

* The host **never opens the prize box**.
* The host **always opens a box that was not selected**.

If the contestant initially chooses the correct box (probability 1/3), the host randomly opens one of the two remaining empty boxes.

If the contestant initially chooses incorrectly (probability 2/3), the host is **forced** to open the only empty box available.

---

# Conditional Probability

Suppose the contestant chooses Box 1 and the host opens Box 3.

Using Bayes' theorem:

[
P(W_1 | H_3) = \frac{P(H_3 | W_1) P(W_1)}{P(H_3)}
]

where

* (P(W_1) = 1/3)
* (P(H_3 | W_1) = 1/2)
* (P(H_3 | W_2) = 1)

After computing the posterior probabilities we obtain

[
P(W_1 | H_3) = \frac{1}{3}
]

and therefore

[
P(W_2 | H_3) = \frac{2}{3}
]

Thus the unopened box that was **not initially chosen** carries probability **2/3**, which explains why switching is advantageous.

---

# Enumeration of All Possible Outcomes

Another way to understand the result is to enumerate all possible cases.

Assume the prize is behind Box 1.

| Initial Choice | Host Opens | Stick Result | Switch Result |
| -------------- | ---------- | ------------ | ------------- |
| Box 1          | Box 2 or 3 | Win          | Lose          |
| Box 2          | Box 3      | Lose         | Win           |
| Box 3          | Box 2      | Lose         | Win           |

Out of the three equally likely possibilities:

* sticking wins in **1 case**
* switching wins in **2 cases**

Therefore

[
P(\text{switch wins}) = \frac{2}{3}
]

---

# Monte Carlo Simulation

Although the analytical solution is straightforward, the Monty Hall problem is famous because the result is **highly counterintuitive**.

For this reason the repository includes **Monte Carlo simulations** to empirically verify the theoretical probabilities.

If the experiment is repeated (N) times, the estimated probabilities are

[
\hat{P}_{stick} = \frac{\text{stick wins}}{N}
]

[
\hat{P}_{switch} = \frac{\text{switch wins}}{N}
]

By the **law of large numbers**:

[
\hat{P}*{stick} \to \frac{1}{3}, \qquad
\hat{P}*{switch} \to \frac{2}{3}
]

as (N \to \infty).

---

# Running the Simulation

### Python

```
python monty_hall.py
```

### Julia

```
julia monty_hall.jl
```

Both implementations run the same experiment and should produce statistically similar results.

---

# Repository Structure

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

# References

Selvin, S. (1975). *A problem in probability.* The American Statistician.

vos Savant, M. (1990). *Ask Marilyn.* Parade Magazine.

Gill, R. (2011). *The Monty Hall Problem is not a probability puzzle.* Statistica Neerlandica.

---

Author: **Alpaslan Kılıç**
