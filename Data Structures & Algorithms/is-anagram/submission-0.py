class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        size = 26
        letters_s = [0] * size
        letters_t = [0] * size

        for i in range(len(s)):
            char_s = ord(s[i]) - 97
            char_t = ord(t[i]) - 97

            letters_s[char_s] += 1
            letters_t[char_t] += 1

        for i in range(26):
            if letters_s[i] != letters_t[i]:
                return False

        return True

