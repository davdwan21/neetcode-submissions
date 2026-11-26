class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        def hoursToEat(speed):
            total = 0
            for i in range(len(piles)):
                total += math.ceil(piles[i] / speed)

            return total

        while l <= r:
            m = int((l + r) / 2)
            curr = hoursToEat(m)
            if curr <= h:
                r = m - 1
            if curr > h:
                l = m + 1
        
        return l
