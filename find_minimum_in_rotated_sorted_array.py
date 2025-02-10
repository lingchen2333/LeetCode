from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while True:
            m = (l+r) //2
            if l == r: 
                return nums[l]
            if nums[m] < nums[r]:
                r=m
            else :
                l = m+1