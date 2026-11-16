class Solution:
    def isValid(self, s: str) -> bool:
        closer_to_opener = {
            ')' : '(',
            '}' : '{',
            ']': '[' 
        }
        stack = []
        for char in s:
            if char not in closer_to_opener:
                stack.append(char)
            else:
                if not stack or stack[-1] != closer_to_opener[char]:
                    return False
                stack.pop()
        return not stack