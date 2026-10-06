class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        big_one = arr[-1]
        l = len(arr)-2
        arr[-1] = -1

        for i in range(l,-1,-1):
            potential = arr[i]
            arr[i] = big_one
            if potential > big_one:
                big_one = potential
        
        return arr