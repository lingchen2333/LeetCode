from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = {(1,0,1,0...): ["cat","tac"], (1,1,0,0...): ["abs"]...} 
        res = defaultdict(list)
        for str in strs:
            characterMap = [0] *26
            for character in str:
                characterMap[ord(character)- ord('a')] += 1
            res[tuple(characterMap)].append(str)
        return list(res.values())

