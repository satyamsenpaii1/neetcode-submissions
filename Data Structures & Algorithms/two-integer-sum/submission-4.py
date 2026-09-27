class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## we could have used two pointer if it was sorted
        ## well we can use sorted function here 
        ## but that'll increase our time complexity

        ## let's do it by hash table

        dict1 = {}
        for i , ele in enumerate(nums):
            complement = target-ele
            if complement in dict1:
                return [dict1[complement],i]
            
            dict1[ele] = i

        return []