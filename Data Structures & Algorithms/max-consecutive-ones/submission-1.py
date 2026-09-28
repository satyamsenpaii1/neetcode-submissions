class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        the_one = 0
        current_one = 0
        lis = []

        for ele in nums:
            if ele == 1:
                current_one+=1

                if current_one > the_one:
                    the_one = current_one
            else:
                current_one = 0
        
        return the_one