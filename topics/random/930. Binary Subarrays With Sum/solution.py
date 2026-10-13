class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        d ={0:1}
        diff =0
        t=0
        s=0

        for i in range(len(nums)):
            s = s+nums[i]

            diff = s- goal
            if diff in d:
                t+=d[diff]

            if s in d:
                d[s] = d[s] + 1
            else:
                d[s] = 1
        return t


        