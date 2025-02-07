class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        left = 0
        right = 1
        currentSet = set()
        maxLength = 0
        for right in range(len(s)):
            while s[right] in currentSet:
                currentSet.remove(s[left])
                left +=1          
            currentSet.add(s[right])
            maxLength = max(maxLength, right -left+1)
        return maxLength


