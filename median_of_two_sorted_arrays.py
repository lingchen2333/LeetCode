from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) ->float:
        total = len(nums1) + len(nums2)
        half = total //2
        A,B = nums1, nums2
        # A is the smaller list
        if len(nums1) > len(nums2):
            A,B = B,A
        # binary search on A
        l=0
        r= len(A) -1
        while True:
            m = (l+r) //2
            Bm = half - m -2

            Aleft = A[m] if m >=0 else float("-infinity")
            Aright = A[m+1] if (m+1) < len(A) else float("infinity")
            Bleft = B[Bm] if Bm >=0 else float("-infinity")
            Bright = B[Bm+1] if (Bm+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total %2 ==0:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
                return min(Aright,Bright)
            
            if Aleft > Bright:
                r = m-1
            else:
                l = m+1