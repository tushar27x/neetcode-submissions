class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n: int = len(numbers)
        l, h = 0, n-1
        while l < h:
            sum_n = numbers[l] + numbers[h]
            
            if sum_n == target:
                return [l+1, h+1]
            elif sum_n > target:
                h -= 1
            else :
                l += 1

        return [-1, -1]