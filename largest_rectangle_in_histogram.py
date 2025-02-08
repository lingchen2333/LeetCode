from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # (height, index)
        maxArea = 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1] < h:
                popH, popI = stack.pop()
                maxArea = max(maxArea, (i - popI) * popH)
                start = popI
            stack.append((h,start))
        
        while stack:
            h,i = stack.pop()
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea


