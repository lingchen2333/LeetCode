from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # {number: frequency}
        numberToFrequency ={}
        for num in nums:
            numberToFrequency[num]  = numberToFrequency.get(num,0) + 1

        frequencyList = [[] for i in range(len(nums)+1)]

        for num, frequency in numberToFrequency.items():
            frequencyList[frequency].append(num)
        
        res = []
        for i in range(len(frequencyList)-1, -1, -1):
            for num in frequencyList[i]:
                res.append(num)
                if len(res) == k:
                    return res
        