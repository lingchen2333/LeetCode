from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # { number: index, }
        numToIndex = {}
        for i in range(len(nums)):
            targetNumber = target - nums[i]
            #check if target number in the map
            if targetNumber in numToIndex:
                return [numToIndex[targetNumber], i]
            
            # add the number to the map
            numToIndex[nums[i]] = i