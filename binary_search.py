from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l=m+1
            else:
                r = m-1
