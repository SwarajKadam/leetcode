class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        lis =[intervals[0][0],intervals[0][1]]
        f = []

        for i in range(1,len(intervals)):
            if intervals[i][0]<=lis[1]:
                if  intervals[i][1]>=lis[1]:

                    lis[1] = intervals[i][1]


            else:
                f.append(lis)
                
                lis = intervals[i]

        f.append(lis)

        return f
            



        