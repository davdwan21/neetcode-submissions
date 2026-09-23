class Solution:
    def search(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        mid = (low + high) // 2

        while low <= high:
            curr = nums[mid]
            if curr == target:
                return mid
            elif curr < target:
                low = mid + 1
            else: # curr > target
                high = mid - 1

            mid = (low + high) // 2

        return -1