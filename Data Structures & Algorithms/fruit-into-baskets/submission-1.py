class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        k = 2
        l = 0
        count = Counter()
        max_fruits = 0
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            while len(count) > k:
                count[fruits[l]] -= 1
                if count[fruits[l]] == 0:
                    del count[fruits[l]]
                l += 1
            
            max_fruits = max(max_fruits, r-l+1)
        
        return max_fruits
