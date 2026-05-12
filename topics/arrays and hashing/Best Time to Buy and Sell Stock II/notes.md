# Best Time to Buy and Sell Stock II — Notes

## Problem Understanding

We are given:

prices[i] = stock price on day i

Goal:

Maximize total profit by buying and selling multiple times.

Rules:
- Can buy and sell multiple times
- Must sell before buying again

---

# Pattern / Category

- Greedy
- Array Traversal

Not:
- DP (for this simple version)
- Sliding Window
- HashMap
- Tree/Graph

---

# Core Greedy Idea

Whenever price increases from one day to the next:

profit opportunity exists.

So:

If:

prices[i+1] > prices[i]

Then add:

prices[i+1] - prices[i]

to total profit.

---

# Intuition

Instead of finding one huge transaction:

buy at 1 → sell at 5

we can think of it as:

1 → 2
2 → 3
3 → 4
4 → 5

Adding all small profits gives same final profit.

Example:

1 → 5 profit:

5 - 1 = 4

Small increases:

(2-1) + (3-2) + (4-3) + (5-4)
= 1 + 1 + 1 + 1
= 4

Same answer.

---

# What Code Is Doing

Loop through array:

For every adjacent pair:

prices[i]
prices[i+1]

If next day price is higher:
- pretend we bought today
- sold tomorrow
- add profit

---

# Example Dry Run

prices = [7,1,5,3,6,4]

---

Day 0:
7 → 1
No profit

profit = 0

---

Day 1:
1 → 5
Profit = 4

profit = 4

---

Day 2:
5 → 3
No profit

profit = 4

---

Day 3:
3 → 6
Profit = 3

profit = 7

---

Day 4:
6 → 4
No profit

Final answer = 7

---

# Why Greedy Works

Any increasing sequence can be split into smaller profitable transactions.

Capturing every positive increase guarantees maximum total profit.

---

# Time Complexity

Single traversal of array:

O(n)

---

# Space Complexity

Only few variables used:

O(1)

---

# Important Interview Explanation

"This is a Greedy problem.

Whenever the next day's price is higher than today's price,
we take that profit immediately.

By summing all positive increases,
we effectively capture the entire upward trend,
which produces the maximum possible profit."

---

# Core Learning

For stock problems:

If unlimited transactions are allowed,
capturing every positive difference is optimal.

Greedy works because local profits combine into global maximum profit.