class Solution:
    def reverseWords(self, s: str) -> str:
        li =[]
        char=''
        for i in s:
            if i != ' ':
                char+=i
            if i == ' ':
                li.append(char)
                char=''
        li.append(char)
        li2= []
        for i in li:
            if i == '':
                continue
            else:
                li2.append(i)
                

        li2.reverse()
        return ' '.join(li2).strip()

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()
        return " ".join(words)