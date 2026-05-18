class Solution:
    def hIndex(self, citations: List[int]) -> int:
        length = len(citations)
        h_index = 0
        for j in range(length,0,-1):
            h= 0
            for i in citations:
                if i >= j:
                    h+=1
            if h>=j:
                h_index= j
                break
        return h_index
                

            