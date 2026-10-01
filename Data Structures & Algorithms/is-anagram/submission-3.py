class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s)!= len(t):
            return False

        dict1= {}
        for ele in s:
            if ele not in dict1:
                dict1[ele] = 1
            else:
                dict1[ele]+=1
        
        for ele in t:
            if ele not in dict1 or dict1[ele] == 0:
                return False
            else:
                dict1[ele] -=1
        return True