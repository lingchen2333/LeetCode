from collections import defaultdict


class Solution:
    def __init__(self):
        self.map = defaultdict(list) # {key:[(value, time),(value,time)]}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((value,timestamp))
    
    def get(self, key: str, timestamp: int) -> str:
        if not self.map[key]:
            return ""
        stack = self.map[key]
        l =0
        r = len(stack)-1
        res = ""
        while l <= r:
            m = (l+r) //2
            if stack[m][1] <= timestamp:
                res = stack[m][0]
                l = m+1
            else:
                r = m-1
        return res
        
