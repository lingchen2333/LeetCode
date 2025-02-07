class Solution:
    def checkInclusion(self, s1: str, s2:str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Count = [0] * 26
        s2Count = [0] * 26

        # a hashmap for s1 and first substring of s2
        for i in range(len(s1)):
            s1Count[ord(s1[i])- ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # compare with the s2 hashmap, when match ==26, they are identical
        match =0
        for i in range(26):
            if s1Count[i] == s2Count[i]:
                match +=1
        
        #iterate through s2
        for left in range(1, len(s2)-len(s1)+1):
            if match == 26: 
                return True
            
            right = left + len(s1)-1
         
            #update the s2Count
            deleteLeftOrd = ord(s2[left-1]) - ord('a')
            s2Count[deleteLeftOrd] -=1
            if s2Count[deleteLeftOrd] == s1Count[deleteLeftOrd]: match +=1
            elif s2Count[deleteLeftOrd] +1 == s1Count[deleteLeftOrd]: match -=1

            addedRightord = ord(s2[right]) - ord('a')
            s2Count[addedRightord] += 1
            if s2Count[addedRightord] == s1Count[addedRightord] : match +=1
            elif s2Count[addedRightord] -1 == s1Count[addedRightord] : match -=1
        return match ==26 

s1="abc"
s2="lecaabee"

mySolution = Solution()
mySolution.checkInclusion(s1,s2)


