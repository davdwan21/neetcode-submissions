class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp = 0
        rp = len(numbers) - 1

        while lp < rp:
            curr_sum = numbers[lp] + numbers[rp]
            if curr_sum < target:
                lp += 1
            elif curr_sum > target:
                rp -= 1
            else: # equal
                return [lp + 1, rp + 1]

        return [-1, -1]