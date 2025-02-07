import collections
import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # use a monotonically decreaing queue  >>>>
        # when the added number is bigger than the last number, pop the last number 
        # else: add the number 

        q = collections.deque() # of index
        res = []
        l = 0
        r = 0

        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # if the largest number in the queue has index > l, pop it
            if l> q[0]:
                q.popleft()
            
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l+=1
        return res
            







        # # using heap, heappush: nlogn time complexity 
        # heap = []
        # #add the first window to the heap, (-num, index)
        # # -num as it is a min heap
        # for i in range(k):
        #     heapq.heappush(heap, (-nums[i],i))
        
        # res = []
        # res.append(-heap[0][0])
        # l = 1
        # for r in range(k, len(nums)):
        #     heapq.heappush(heap, (-nums[r], r))
        #     # while the maximum number is out of bound, pop it from the heap
        #     while heap[0][1] < l:
        #         heapq.heappop(heap)
        #     res.append(-heap[0][0])
        #     l += 1
        # return res

