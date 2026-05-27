class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps_to_reach_last = len(nums)-1
        flag = True
        i = 0
        diff =0
        while flag:
            big_jump =0
            
            if jumps_to_reach_last - nums[i]<=0:
                return True
            if nums[i] == 0:
                return False
            for j in range(i+1,nums[i]+1+i):
                if j>=len(nums):
                    continue
                if big_jump<=nums[j]+j:

                    big_jump = nums[j]+j
                    diff= j-i
                
            jumps_to_reach_last -= diff
            i+=diff
            
            if jumps_to_reach_last ==0:
                return True

