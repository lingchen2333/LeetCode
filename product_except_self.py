from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        productBefore = []
        productAfter = [0] * len(nums)
        
        currentProduct = 1
        for i in range(len(nums)-1,-1,-1):
            productAfter[i] =currentProduct
            currentProduct *= nums[i]
        res = []
        currentProduct = 1
        for i in range(len(nums)):
            productBefore.append(currentProduct)
            currentProduct *= nums[i]
            res.append(productAfter[i] * productBefore[i])
        return res
        
        
