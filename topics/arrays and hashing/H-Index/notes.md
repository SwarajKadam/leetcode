# 274. H-Index — Notes

## Problem Understanding

We are given:

citations[i] = number of citations for ith paper

Goal:

Find the maximum value h such that:

- researcher has at least h papers
- each of those papers has at least h citations

---

# Pattern / Category

- Sorting
- Greedy Observation
- Counting

Not:
- DP
- Sliding Window
- Tree/Graph
- HashMap

---

# Core Observation

If array is sorted in descending order:

The index itself tells us how many papers we have considered.

At index i:

papers = i + 1

Now check:

citations[i] >= papers

If true:
- there are at least (i+1) papers
- each having at least (i+1) citations

Which exactly matches h-index definition.

---

# Brute Force Idea

Try every possible h value.

For each h:
- count how many papers have citations >= h

If:

count >= h

then h is valid.

Take maximum valid h.

---

# Brute Force Complexity

Outer loop:
O(n)

Inner counting loop:
O(n)

Total:

O(n²)

Space:
O(1)

---

# Optimal Approach

## Step 1

Sort citations in descending order.

Example:

[3,0,6,1,5]

becomes:

[6,5,3,1,0]

---

## Step 2

Traverse array.

At each index:

papers = i + 1

Check:

citations[i] >= papers

If true:
- valid h-index candidate found

Update answer.

Else:
- stop traversal

---

# Dry Run

citations = [3,0,6,1,5]

After sorting:

[6,5,3,1,0]

| i | citations[i] | papers (i+1) | valid? |
|---|---|---|---|
|0|6|1|yes|
|1|5|2|yes|
|2|3|3|yes|
|3|1|4|no|

Largest valid value = 3

Answer = 3

---

# Why Sorting Helps

After sorting descending:

All papers before index i
have citations >= citations[i]

So if:

citations[i] >= i+1

then automatically:
- first (i+1) papers all satisfy h-index condition

No extra counting needed.

---

# Time Complexity

Sorting:
O(n log n)

Traversal:
O(n)

Total:
O(n log n)

---

# Space Complexity

Depends on sorting implementation:

Usually:
O(1) or O(n)

---

# Important Interview Explanation

"This is mainly a sorting + greedy observation problem.

After sorting in descending order,
the index represents how many papers are being considered.

If citations[i] >= i+1,
then there are at least (i+1) papers
having at least (i+1) citations.

The maximum such value is the h-index."

---

# Core Learning

Sorting can transform repeated counting problems
into direct index-based checks.

Index often represents quantity/count after sorting.