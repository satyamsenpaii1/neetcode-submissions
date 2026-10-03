class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word=""
        max_len = max(len(word1),len(word2))
        counter = 0
        while counter < max_len:
            if len(word1)-1 >= counter:
                word+=word1[counter]
            if len(word2)-1 >= counter:
                word+=word2[counter]
            counter+=1

        return word