# Pattern: Hashing

##  When to Use
- Detect duplicates
- Count frequency
- Fast lookup problems


## Common Problems
- Contains Duplicate
- Two Sum
- Group Anagrams


## Template Code

### Using Set
```python
seen = set()
for x in arr:
    if x in seen:
        return True
    seen.add(x)