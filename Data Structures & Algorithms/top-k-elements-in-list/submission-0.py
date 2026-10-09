class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for ele in nums:
            if ele not in dict1:
                dict1[ele] = 1
            else:
                dict1[ele]+=1
        
        lis1 = list(dict1.keys())
        result = []

        while k > 0 and len(lis1) != 0:
            max_value = lis1[0]

            for num in lis1:
                if dict1[num] > dict1[max_value]:
                    max_value =num
                
            result.append(max_value)
            lis1.remove(max_value)
        
            k-=1
        
        return result