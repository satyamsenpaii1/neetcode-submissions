class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        second = len(heights)-1

        max_water = 0

        while first<second:
            current_water = ((second-first) * min(heights[first],heights[second]))
            if current_water >= max_water:
                max_water = current_water

            if heights[first] < heights[second]:
                first+=1
            else:
                second-=1

        return max_water