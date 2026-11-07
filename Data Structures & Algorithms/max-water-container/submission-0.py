class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            w = abs(j - i)
            h = min(heights[i], heights[j])
            area = w * h
            ans = max(ans, area)
            
            if heights[i] < heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -= 1
            else: # equal
                i += 1

        return ans
        