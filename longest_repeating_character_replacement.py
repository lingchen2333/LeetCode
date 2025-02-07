from collections import defaultdict

class Solution:
    def characterReplacement(self, s:str, k: int) -> int:
        # max count + k > length
        left =0
        maxCount = 0
        characterToCount = defaultdict(int)
        maxLength = 0

        for right in range(len(s)):
            # add to characterCount
            characterToCount[s[right]] += 1
            # update maxCount
            maxCount = max(maxCount, characterToCount[s[right]])

            # if need to replace more than k letters
            if maxCount + k < right - left +1:
                # left ++, pop the left most character
                characterToCount[s[left]] -= 1
                left +=1
            maxLength = max(maxLength, right - left +1)
        return maxLength

