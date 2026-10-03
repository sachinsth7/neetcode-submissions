class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for ag in strs:
            key = ''.join(sorted(ag))
            anagrams[key].append(ag)
        return list(anagrams.values())