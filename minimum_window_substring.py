class Solution:
    def minWindow(self, s:str, t:str) ->str:
        # hash map for t
        tCount = {}
        for c in t:
            tCount[c] = tCount.get(c,0) +1
        
        #hash map for the sliding window
        windowCount = {}

        need = len(tCount)
        have = 0

        l = 0
        res =[-1,-1]
        minlength = float("infinity")
        # iterate through right
        for r in range(len(s)):
            rightC = s[r]
            windowCount[rightC] = windowCount.get(rightC,0) + 1

            if rightC in tCount and windowCount[rightC] == tCount[rightC]:
                have +=1
            
            # increase left if have == need
            while have == need:
                # remove the left from windowCount, check if it impacts have
                leftC = s[l]
                windowCount[leftC] -= 1

                if leftC in tCount and windowCount[leftC] +1 == tCount[leftC]:
                    have -=1
                else: 
                    if r -l +1 < minlength:
                        minlength = r - l +1
                        res = [l,r]
                left += 1
        
        l,r = res[0], res[1]
        if minlength != float("infinity"):
            return s[l:r+1]
        return ""
