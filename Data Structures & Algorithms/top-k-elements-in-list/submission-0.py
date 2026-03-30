class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counts = {}
        for n in nums:
            num_counts[n] = 1 + num_counts.get(n, 0)
        
        t_num_counts = list(num_counts.items())
        _result = sorted(t_num_counts, key=lambda tup: tup[1], reverse=True)[:k]
        return [r[0] for r in _result ]



