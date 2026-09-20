class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            look_for = target - nums[i]
            if look_for in seen:
                return [seen[look_for], i]
            seen[nums[i]] = i