## Link
https://leetcode.com/problems/valid-anagram/description/

## Problem Summary
- Input:   s: str, t: str
- Output:  bool
- Goal in 1 line: check whether 2 strings are anagram

## Intuition (Very Important)
We need to check if given 2 strings are anagram.


## Approach
Step-by-step:
1. class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s ={}
        dict_t ={}
        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i]+=1
        for j in t:
            if j not in dict_t:
                dict_t[j] =1
            else:
                dict_t[j]+=1
        return dict_s == dict_t
         - Time Complexity: O(n+m) and Space: O(n + m) in worst case
2. class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s ={}
        dict_t ={}
        for i in s:
            if i not in dict_s:
                dict_s[i] = 1
            else:
                dict_s[i]+=1
        for j in t:
            if j not in dict_t:
                dict_t[j] =1
            else:
                dict_t[j]+=1
        return dict_s == dict_t
        

        Time Complexity: O(n+n) and Space Complexity: O(n+n) or just O(n)


3. class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1
            if count[ch] < 0:
                return False

        return True


        Time Complexity: O(n) and Space Complexity: O(n)  

4. class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        Time Complexity: O(nlogn) and Space Complexity: O(n)

## Pattern Used
Hashing

## Key Takeaways
If problem asks for anagram → think of sorting and comparing or comparing dicts first.