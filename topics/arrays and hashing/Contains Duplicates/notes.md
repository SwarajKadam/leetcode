## Link
https://leetcode.com/problems/contains-duplicate/description/

## Problem Summary
- Input:   nums: List[int]
- Output:  bool
- Goal in 1 line: if duplicate in nums return true else false

## Intuition (Very Important)
We need to check if any number appears more than once.
Brute force would be O(n^2), so we optimize using hashing.


## Approach
Step-by-step:
1. brute for - used nested for loop but - Time Complexity: O(n²) and Space Complexity: O(1)
2. class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict_nums = {}
        for i in nums:
            if i not in dict_nums:
                dict_nums[i] = 1
            else:
                dict_nums[i] = dict_nums[i] +1
        for i in dict_nums:
            if dict_nums[i] > 1:
                return True
        return False

        Time Complexity: O(n) and Space Complexity: O(n)


3. class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        Time Complexity: O(n) and Space Complexity: O(n)
            

## Pattern Used
Hashing

## Key Takeaways
If problem asks for duplicate detection → think SET first