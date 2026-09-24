class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        lis = strs[0]

        for word1 in strs[1:]:
            word = []

            for letter in range(min(len(lis), len(word1))):
                if word1[letter] == lis[letter]:
                    word.append(word1[letter])
                else:
                    break

            lis = ''.join(word)

            if not lis:
                return ""

        return lis