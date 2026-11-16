class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t not in operator:
                stack.append(t)
            else:
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if t == '+':
                    result = op2 + op1
                elif t == '-':
                    result = op2 - op1
                elif t == '/':
                    result = int(op2 / op1)
                else:
                    result = op2 * op1
                stack.append(result)
        return int(stack[-1])