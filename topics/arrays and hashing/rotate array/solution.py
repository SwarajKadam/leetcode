class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        popped =None
        k = k % len(nums)
        li=[]
        for i in range(0,k):
            if len(nums)!=0:

                popped = nums.pop()
                li.append(popped)

        li.reverse()

        nums[:] = li+nums
    

        