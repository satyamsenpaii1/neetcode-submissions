class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        wrt_ptr = 0
        temp_list = []
        counter = 0

        for ele in nums:
            if ele == val:
                temp_list.append(ele)
            else:
                nums[wrt_ptr] = ele
                wrt_ptr+=1
        counter = wrt_ptr
        nums[wrt_ptr:] = temp_list

        return counter