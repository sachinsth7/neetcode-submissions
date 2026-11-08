class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += str(len(s)) + '%' + s
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        j = 0
        while i < len(s):
            while s[i] != '%':
                i = i + 1
            length = int(s[j:i])
            start = i + 1
            end = start + length
            decoded.append(s[start:end])
            i = end
            j = i
        return decoded