class Solution:
    def isValid(self, s: str) -> bool:
        closer_to_opener = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        stack = []
        for ch in s:
            if ch not in closer_to_opener:
                stack.append(ch)
            else:
                if not stack:
                    return False
                element = stack.pop()
                if closer_to_opener.get(ch) != element:
                    return False
        return not stack