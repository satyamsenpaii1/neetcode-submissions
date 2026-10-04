class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ## Since the only first k elements are signicifcant and remaning ones 
        ## does not matter we can just put k elements and not care about
        ## remaining ones

        wrt_pointer = 0
        for ele in nums:
            if ele != val:
                nums[wrt_pointer] = ele
                wrt_pointer+=1
        
        return wrt_pointer