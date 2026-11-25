class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(list(s))
        t_count = Counter(list(t))
        return s_count == t_count
