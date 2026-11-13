class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        result = max_k

        while min_k <= max_k:
            k = (min_k + max_k) // 2
            total_time = 0

            for pile in piles:
                total_time += math.ceil(pile / k)

            if total_time > h:
                min_k = k + 1
            else:
                max_k = k - 1
                result = k
        
        return result
        