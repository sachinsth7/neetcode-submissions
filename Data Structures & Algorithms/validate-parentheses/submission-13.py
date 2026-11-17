class Solution:
    def isValid(self, s: str) -> bool:
        closer_to_opener = {
            ']' : '[',
            '}' : '{',
            ')' : '('
        }
        stack = []
        for ch in s:
            if ch not in closer_to_opener:
                stack.append(ch)
            else:
                if not stack or stack[-1] != closer_to_opener[ch]:
                    return False
                stack.pop()
        return not stack