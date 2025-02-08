from typing import List


class Solution:
    def evalRPN(self,tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):

            if tokens[i] in set(['+', '-', '*', '/']):
                num2 = stack.pop()
                num1 = stack.pop()  
                if tokens[i] == '+':
                    stack.append(num1+num2)
                elif tokens[i] == '-':
                    stack.append(num1-num2)
                elif tokens[i] == '*':
                    stack.append(num1*num2)
                elif tokens[i] == '/':
                    stack.append(int(float(num1)/num2))
            else:
                stack.append(int(tokens[i]))
        
        return stack[0]

tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
mysolution = Solution()
print(mysolution.evalRPN(tokens))