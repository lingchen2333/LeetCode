from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       characterMapToWords = defaultdict(list) #create an empty list as values for the key
    
       for s in strs:
            characterMap = [0] * 26
            for character in s:
               characterMap[ord(character) - ord('a')] += 1
            characterMapToWords[tuple(characterMap)].append(s)
       return list(characterMapToWords.values())
           

