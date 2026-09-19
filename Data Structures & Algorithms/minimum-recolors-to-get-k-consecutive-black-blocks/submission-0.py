class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start = 0
        min_rep = len(blocks) + 1
        count = 0
        for end in range(len(blocks)):
            if blocks[end] == 'W':
                count += 1
            
            if (end-start + 1) >= k:
                min_rep = min(count, min_rep)
                if blocks[start] == 'W':
                    count -= 1
                
                start += 1
        
        return min_rep