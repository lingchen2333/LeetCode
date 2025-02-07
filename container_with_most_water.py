from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        res =0
        while left < right:
            res = max(res, min(heights[left],heights[right])* (right-left))
            if heights[left] < heights[right]:
                left +=1
            else: right -=1
        return res