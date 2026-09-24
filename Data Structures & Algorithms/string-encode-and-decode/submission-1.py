class Solution:
    # probably expected time complexity is O(n)

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            length = len(s)
            encoded += f"{length}*{s}"
        
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        pointer = 0
        res = []

        while pointer < len(s):
            length = ""
            while s[pointer] != "*":
                length += s[pointer]
                pointer += 1
                
            length = int(length)
            word = s[(pointer + 1):(pointer + length + 1)]
            res.append(word)
            pointer += (1 + length)

        print(res)
        return res

