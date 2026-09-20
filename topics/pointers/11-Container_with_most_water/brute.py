class Solution:
    def maxArea(self, height: list[int]) -> int:
        area = 0
        for i in range(0,len(height)-1):
            for j in range(i+1,len(height)):
                if height[i]<height[j]:
                    l =height[i]
                else:
                    l=height[j]

                b = j-i

                a=l*b
                if a>area:
                    area = a
                
        return area
        