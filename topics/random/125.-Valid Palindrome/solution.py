class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned_text = ''.join([char for char in s if char.isalnum()])
        p=''
        l=[]

        for i in range(len(cleaned_text)-1,-1,-1):
            l.append(cleaned_text[i])
        p=''.join(l)

        if p==cleaned_text:
            return True
        else:
            return False
        