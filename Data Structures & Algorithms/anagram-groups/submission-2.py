class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}

        for ele in strs:
            key = "".join(sorted(ele))
            if key not in dict1:
                dict1[key] = []
                dict1[key].append(ele)
            
            else:
                dict1[key].append(ele)
        
        return list(dict1.values())