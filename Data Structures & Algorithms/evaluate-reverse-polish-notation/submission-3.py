class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ch = ['+', '-', '*', '/']
        for e in tokens:
            if e not in ch:
                stack.append(int(e))
            else:
                right = stack.pop()
                left = stack.pop()
                if e == '+':
                    result = left + right
                elif e == '-':
                    result = left - right
                elif e == '*':
                    result = left * right
                else: 
                    result = int(left/right)
                stack.append(result)
        result = stack[-1]
        return result