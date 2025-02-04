from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # 23#...1#...
        # number represents the length of the string
        encodedString = ""
        for s in strs:
            encodedString += str(len(s)) + '#' + s
        return encodedString
    
    def decode(self, s: str) -> List[str]:
        decodedStrings = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            number = int(s[i:j])
            decodedStrings.append(s[j+1:j+1+number])
            i = j+number+1
        return decodedStrings

