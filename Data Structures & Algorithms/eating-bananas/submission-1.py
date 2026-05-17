class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (right + left) // 2

            total = 0
            for pile in piles:
                total += math.ceil(pile / mid)


            if total <= h:
                right = mid

            else:
                left = mid + 1



        return left
