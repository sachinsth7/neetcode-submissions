class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for ga in strs:
            key = ''.join(sorted(ga))
            anagrams[key].append(ga)
        return list(anagrams.values())