class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
            
        target = strs[0]
        counter = 0
        
        while True:
            for ele in strs:
                if counter>=len(ele) or ele[counter]!= target[counter]:
                    return target[:counter]
            counter+=1
        