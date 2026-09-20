class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        lis = list(s.split())
        return len(lis[-1])