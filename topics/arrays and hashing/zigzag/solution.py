class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        reverse =False
        li = []
        li2=[]
        for i in range (0,numRows):
            li.append([])


        n = 0
        for letter in s:
            new_li = li[n]
            new_li.append(letter)
            if n==0:
                reverse = True
            if n == numRows-1:
                reverse= False
            if reverse== True:
                n+=1
            if reverse== False:
                n-=1

        for i in li:
            lis = ''.join(i)
            li2.append(lis)

        return ''.join(li2)


        