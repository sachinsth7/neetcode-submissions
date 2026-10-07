class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                right = stack.pop()
                left = stack.pop()
                if t == "+":
                    num = int(left) + int(right)
                elif t == "-":
                    num = int(left) - int(right)
                elif t == "*":
                    num = int(left) * int(right)
                else:
                    num = int(left) / int(right)
                stack.append(num)
        return int(stack[-1]) 