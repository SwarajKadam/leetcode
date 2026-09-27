class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [['']]
        d ={}
        for index in range(0,len(strs)):
            text = ''.join(sorted(strs[index]))
            if text in d:
                lis = d[text]
                lis.append(strs[index])
            else:
                d[text] = [strs[index]]
        final_lis = []
        for k,v in d.items():
            final_lis.append(v)

        return final_lis


            

        