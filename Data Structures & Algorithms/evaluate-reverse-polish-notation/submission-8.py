class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t not in operands:
                stack.append(t)        
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                if t == '+':
                    result = left + right
                elif t == '-':
                    result = left - right
                elif t == '*':
                    result = left * right 
                else:
                    result = left / right
                stack.append(result)
        return int(stack[-1])