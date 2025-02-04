from typing import List


class Solution:
    def longestConsecutive(self, nums:List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num-1 not in numSet:
                currNum = num
                count =1
                while currNum+1 in numSet:
                    count += 1
                    currNum += 1
                res = max(res, count)
        return res
