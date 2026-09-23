class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # understanding: instead of searching a list of dictionary, we use the character count itself as a hashable key
        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            groups[tuple(count)].append(s)
        return list(groups.values())

        # naiive:
        """if len(strs) == 1:
            return [strs]

        seen = []
        res = []

        for string in strs:
            char_count = {}
            for char in string:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1

            added_flag = False
            for i, seen_string in enumerate(seen):
                if char_count == seen_string:
                    res[i].append(string)
                    added_flag = True

            if added_flag:
                continue

            res.append([string])
            seen.append(char_count)

        return res"""



