from typing import List

class Solution:
    def trap(self, height:List[int]) ->int :
        res =[0] * len(height)
        # find the max height to the left of each bar
        leftMax =height[0]
        for i in range(1,len(height)):
            leftMax = max(leftMax, height[i-1]-1)
            res[i] = leftMax
        # find the max height to the right of each bar
        # and take the min of rightMax and leftMax
        rightMax = height[-1]
        for i in range(len(height)-2,0,-1):
            rightMax = max(rightMax, height[i+1])
            wallMax = min(res[i],rightMax)
            if height[i] >= wallMax:
                res[i] = 0
            else: res[i] = wallMax - height[i]
        return sum(res)
        
