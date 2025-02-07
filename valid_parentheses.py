class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOPen = {')': '(',
                       '}' : '{',
                       ']' : '['}
        for c in s:
            if c in closeToOPen: # c is close
                if stack and stack[-1] == closeToOPen[c]:
                    stack.pop()
                else: return False
            else: stack.append(c)

        return len(stack) == 0

s="[(])"    
mysolution = Solution()
mysolution.isValid(s)