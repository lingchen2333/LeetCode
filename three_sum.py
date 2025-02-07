from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # exit loop when number is positive
            if num > 0 :
                break
            # skip number that is the same as the previous one
            if i and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) -1
            target = -num
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else: 
                    res.append([num,nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1

        return res

