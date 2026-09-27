class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(ele.lower() for ele in s if ele.isalnum())

        first=0
        second=len(s1)-1

        while first<second:
            if s1[first] != s1[second]:
                return False
            else:
                first+=1
                second-=1
        return True
        