class Solution:
    def maxArea(self, height: list[int]) -> int:
        L = 0
        R = len(height)-1
        a=0
        while L<R:
            
            l = min(height[L],height[R])
            b = R-L
            area = l*b
            if area>a:
                a = area
            if height[L]<=height[R]:
                L=L+1
            else:
                R=R-1
            

        return a
        