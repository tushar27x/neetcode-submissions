class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count: int = 0
        freq_map: dict[int, int] = {}
        for n in nums:
            freq_map[n] = freq_map.get(n, 0) + 1
        
        return [k for k, v in sorted(freq_map.items(), key = lambda x: x[1], reverse = True)[:k]]