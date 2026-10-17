class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = len(nums)-1
        mid = int(l/2)
        left = 0
        right =l

        while left<=right:
            if nums[mid]<target:
                left = mid+1

                mid = int((left+right)/2)
                
            elif nums[mid]>target:
                right =mid-1
                mid =  int((left+right)/2)

            else:
                return mid

           
        return -1

            

        