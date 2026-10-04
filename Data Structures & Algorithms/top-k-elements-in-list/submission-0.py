class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = Counter(nums)

        buckets = [[] for i in range(len(nums) + 1)]

        for num, freq in num_to_freq.items():
            buckets[freq].append(num)
        
        result = []
        for bucket in buckets[::-1]:
            for num in bucket:
                if k > 0:
                    result.append(num)
                    k -= 1
        
        return result
