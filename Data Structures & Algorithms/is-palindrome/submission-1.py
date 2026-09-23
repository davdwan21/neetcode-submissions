class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True

        lp = 0
        rp = len(s) - 1
        while lp < rp:
            l_char = s[lp]
            while l_char.isalnum() == False and lp < rp:
                lp += 1
                l_char = s[lp]
            
            r_char = s[rp]
            while r_char.isalnum() == False and lp < rp:
                rp -= 1
                r_char = s[rp]

            if r_char.lower() != l_char.lower():
                return False
            
            lp += 1
            rp -= 1

        return True