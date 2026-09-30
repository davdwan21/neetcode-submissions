class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # comparing every substring O(n^2)
        max_len = 0
        l = 0
        curr_chars = set() # keys: chars, values: placeholder

        for r in range(len(s)):
            while s[r] in curr_chars:
                curr_chars.remove(s[l])
                l += 1
            curr_chars.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
        
                

