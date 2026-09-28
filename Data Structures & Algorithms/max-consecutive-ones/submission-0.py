class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_one = 0
        lis = []
        for ele in nums:
            if ele == 1:
                max_one+=1
            else:
                lis.append(max_one)
                max_one=0
        if max_one:
            lis.append(max_one)
        
        return max(lis)