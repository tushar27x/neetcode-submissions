class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        dict = {}
        for c in arr:
            freq = dict.get(c, 0)
            dict[c] = freq+1
        
        distinct_chars = [c for c in arr if dict[c] == 1]
        if len(distinct_chars) < k:
            return ""
        
        return distinct_chars[k-1]