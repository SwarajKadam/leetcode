class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        target = k
        required= 0
        counter = 0
        for i in range(len(nums)):
            required = target - nums[i]
            target = required
            if target==0:
                    counter+=1
                    
                    
            j = i+1
            
                    
            while j<len(nums):
                required = target - nums[j]
                target = required
                if target==0:
                    counter+=1
                j=j+1
            target = k
            
                    
        return counter

        