# Gas Station — Notes

## Problem Understanding

We are given:

- `gas[i]` → fuel available at station `i`
- `cost[i]` → fuel needed to travel from station `i` to `i+1`

Goal:

Find the starting station index from which we can complete the full circular journey.

If impossible, return `-1`.

---

# Pattern / Category

- Greedy
- Running Sum / Prefix Sum intuition

Not:
- DP
- Sliding Window
- Tree/Graph
- HashMap

---

# Brute Force Approach

## Idea

Try every station as the starting point.

For each start:
- simulate the entire circular journey
- maintain fuel tank
- if tank becomes negative → fail
- if full circle completed → return start

---

## Intuition

At every station:

1. Add current station gas
2. Pay travel cost
3. If tank < 0 → cannot continue

---

## Time Complexity

For every starting station:
- we may travel through all stations

So:

O(n * n) = O(n²)

---

## Space Complexity

O(1)

---

## Why Brute Force Gets TLE

Because we repeatedly retry many bad starting positions.

Example:

start 0 → fail late  
start 1 → fail late  
start 2 → fail late  

Many repeated traversals happen.

---

# Optimal Greedy Approach

## Main Observation

If starting from station `start` fails at station `i`:

Then NO station between `start` and `i`
can be a valid starting station.

Reason:

If we already failed after accumulating fuel from previous stations,
then starting from the middle would give even less fuel.

So we can skip all those stations directly.

---

# Key Variables

## total_tank

Tracks:

sum(gas) - sum(cost)

Used to check if completing the circuit is possible overall.

If:

total_tank < 0

then answer is impossible.

---

## current_tank

Tracks fuel from current chosen start.

If:

current_tank < 0

then current start failed.

Move start to:

i + 1

and reset current_tank to 0.

---

## start

Current candidate starting station.

---

# Greedy Logic

For each station:

gain = gas[i] - cost[i]

Update:

current_tank += gain
total_tank += gain

If:

current_tank < 0

Then:
- current start is invalid
- all stations between start and i are invalid
- next possible start = i + 1

Reset:

current_tank = 0

---

# Why Greedy Works

Suppose:

start = A

We successfully travel:

A → A+1 → ... → B

but fail after B.

This means:
- A cannot be answer
- A+1 cannot be answer
- A+2 cannot be answer
...
- B cannot be answer

So we directly jump to:

B + 1

instead of checking all intermediate starts.

This removes repeated work.

---

# Time Complexity

Single pass through array:

O(n)

---

# Space Complexity

O(1)

---

# Important Interview Explanation

"This is a Greedy problem.

The key observation is:
if a starting station fails at index i,
then every station between the current start and i also fails.

Therefore we can greedily skip all of them
and move the start directly to i + 1.

We also maintain total fuel balance to check
whether completing the circuit is possible overall."

---

# Dry Run Summary

Example:

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

gain = [-2,-2,-2,+3,+3]

current_tank becomes negative at:
- station 0
- station 1
- station 2

So we keep shifting start:

0 → 1 → 2 → 3

Starting from 3 succeeds.

Answer = 3

---

# Core Learning

Time complexity depends on total operations,
NOT on how many loops are written.

Even a single while loop can behave like O(n²)
if it repeatedly retries work.