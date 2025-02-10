from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateHours(speed, piles) -> int:
            hour = 0
            for pile in piles:
                hour += ceil(pile/speed)
            return hour
         
        l = max(piles)
        s = 1
        minSpeed = l
        
        while s <= l:
            m = (l+s) //2
            hNeed = calculateHours(m,piles)
            if hNeed > h: # takes longer, need to increase speed
                s = m+1
            elif hNeed <= h: #takes shorter, could be the minspeed, test out smaller speed
                minSpeed= min(minSpeed,m)
                l = m-1

        return minSpeed

       
            