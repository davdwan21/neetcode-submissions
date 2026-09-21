class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        lookup = {num: 0 for num in nums}
        max_len = 1

        for num, tried in lookup.items():
            if tried == 1:
                continue

            cnt = num + 1
            length = 1
            while cnt in lookup:
                lookup[cnt] = 1
                length += 1
                cnt += 1

            if length > max_len:
                max_len = length

        return max_len

            


            