class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        substrings = set()

        for ele in words:
            for x in words:
                if len(ele) < len(x):
                    if ele in x:
                        substrings.add(ele)
    
        return list(substrings)