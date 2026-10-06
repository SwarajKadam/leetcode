class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        counter = 0
        sum = 0

        for i in range(len(nums)):
            sum +=nums[i]
            diff = sum -k
            if diff in d:
                counter = counter + d[diff]
                
            d[sum] = d.get(sum, 0) + 1

        return counter

        