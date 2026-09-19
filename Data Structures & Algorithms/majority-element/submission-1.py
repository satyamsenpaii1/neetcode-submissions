class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for ele in nums:
            if ele in dict1:
                dict1[ele]+=1
            else:
                dict1[ele]=1

        inti=0
        count=0
        for ele in dict1:
            if dict1[ele] > count:
                inti = ele
                count = dict1[ele]
            
        return inti