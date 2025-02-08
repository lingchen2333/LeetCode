from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonically decreasing stack (temp, index)
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i],i)) 
        return res

temperatures = [30,38,30,36,35,40,28]
print(Solution().dailyTemperatures(temperatures))