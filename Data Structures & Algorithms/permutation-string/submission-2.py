class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        if s1_len> len(s2):
            return False
        count = {}        
        left = 0
        window = {}
        for i in range(s1_len):
            count[s1[i]] = count.get(s1[i], 0) + 1
        for right in range(len(s2)):
            ch = s2[right]
            window[ch] = window.get(ch, 0) + 1
            if right -left + 1 > s1_len:
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
            if count == window:
                return True
        return False

            

        