from typing import List


class Solution:
    def carFleet(self, target:int, position: List[int], speed: List[int]) -> int:
        postionAndTime = [] #(pos, time)
        for i in range(len(position)):
            pos = position[i]
            v = speed[i]
            postionAndTime.append((pos,(target- pos)/v))
        postionAndTime.sort(reverse=True) 
        stack = []
        for pos,time in postionAndTime:
            if not stack or (stack and time > stack[-1]):
                stack.append(time)
        return len(stack)
            