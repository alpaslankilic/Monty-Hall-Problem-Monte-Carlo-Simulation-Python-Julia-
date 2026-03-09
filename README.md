# Monty Hall Problem — Monte Carlo Simulation

This repository presents a **Monte Carlo simulation of the Monty Hall problem** together with a **formal probabilistic analysis**. The goal is to compare the theoretical probabilities derived from probability theory with empirical results obtained through large scale simulations.

The simulation is implemented in **Python and Julia**, and both implementations reproduce the same probabilistic experiment.

---

# The Monty Hall Problem

The Monty Hall problem is one of the most famous paradoxes in probability theory. It is named after **Monty Hall**, the host of the television game show *Let's Make a Deal*.

The game proceeds as follows:

1. A contestant faces **three closed boxes**.
2. Exactly **one box contains a prize**, while the other two are empty.
3. The contestant selects one box.
4. The host, who **knows where the prize is**, opens one of the remaining boxes that **does not contain the prize**.
5. The contestant is then offered a choice:

* **Stick** with the original box
* **Switch** to the other unopened box

The fundamental question is

> Does switching improve the probability of winning?

Many people believe that once one empty box is opened the remaining two boxes should each have probability 1/2. However this reasoning ignores the **information contained in the host's action**.

---

# Theoretical Result

The optimal strategy is **switching boxes**.

| Strategy | Probability of Winning |
| -------- | ---------------------- |
| Stick    | $\frac{1}{3}$          |
| Switch   | $\frac{2}{3}$          |

Switching therefore **doubles the probability of winning**.

---

# Probabilistic Model

Let

* $W_i$ denote the event that the prize is behind box $i$
* $H_j$ denote the event that the host opens box $j$

Assume the contestant initially selects **Box 1**.

The prior probabilities are

$$
P(W_1) = P(W_2) = P(W_3) = \frac{1}{3}
$$

The host follows two deterministic rules:

* The host **never opens the prize box**.
* The host **never opens the box selected by the contestant**.

If the contestant initially chooses the correct box (probability $1/3$), the host randomly opens one of the two remaining empty boxes.

If the contestant initially chooses incorrectly (probability $2/3$), the host is **forced** to open the only empty box available.

---

# Conditional Probability Analysis

Suppose the contestant selects Box 1 and the host opens Box 3.

Using **Bayes' theorem**

$$
P(W_1 \mid H_3) = \frac{P(H_3 \mid W_1) P(W_1)}{P(H_3)}
$$

where

$$
P(W_1) = \frac{1}{3}
$$

$$
P(H_3 \mid W_1) = \frac{1}{2}
$$

$$
P(H_3 \mid W_2) = 1
$$

Computing the posterior probability yields

$$
P(W_1 \mid H_3) = \frac{1}{3}
$$

and therefore

$$
P(W_2 \mid H_3) = \frac{2}{3}
$$

Thus the unopened box that was **not initially chosen** carries probability $2/3$, which explains why switching is advantageous.

---

# Enumeration of Possible Outcomes

Another way to understand the result is to enumerate all possible scenarios.

Assume the prize is behind Box 1.

| Initial Choice | Host Opens | Stick Result | Switch Result |
| -------------- | ---------- | ------------ | ------------- |
| Box 1          | Box 2 or 3 | Win          | Lose          |
| Box 2          | Box 3      | Lose         | Win           |
| Box 3          | Box 2      | Lose         | Win           |

Out of the three equally likely possibilities

* sticking wins in **1 case**
* switching wins in **2 cases**

Therefore

$$
P(\text{switch wins}) = \frac{2}{3}
$$

---

# Monte Carlo Simulation

Although the analytical solution is straightforward, the Monty Hall problem is famous because the result is **highly counterintuitive**. For this reason we verify the theoretical result using simulation.

If the experiment is repeated $N$ times, the empirical probabilities are

$$
\hat{P}_{stick} = \frac{\text{stick wins}}{N}
$$

$$
\hat{P}_{switch} = \frac{\text{switch wins}}{N}
$$

By the **law of large numbers**

$$
\hat{P}*{stick} \rightarrow \frac{1}{3}, \qquad
\hat{P}*{switch} \rightarrow \frac{2}{3}
$$

as $N \rightarrow \infty$.

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

Both implementations perform the same experiment and produce statistically consistent results.

---

# Repository Structure

```
monty-hall-simulation
│
├── python
│   └── monty_hall.py
|   └── code_explanation.md
|   └── result.png
│
├── julia
│   └── monty_hall.jl
|   └── code_explanation.md
|   └── result.png
```
Author: **Alpaslan Kılıç**
