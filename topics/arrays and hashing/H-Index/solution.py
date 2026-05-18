class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse =True)
        h_index =0
        for i in range(len(citations)):
            papers = i + 1

            if citations[i] >= papers:
                h_index = papers
            else:
                break

        return h_index
        
                

            