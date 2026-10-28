class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        sorted_data =sorted(intervals, key=lambda x: x[1])
        count=0

        initial = sorted_data[0]

        for i in range(1,len(sorted_data)):
            if sorted_data[i][0] < initial[1]:
                count+=1
            else:
                initial = sorted_data[i]

        return count
        