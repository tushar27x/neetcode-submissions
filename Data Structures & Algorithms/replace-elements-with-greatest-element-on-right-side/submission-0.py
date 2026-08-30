class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [-1] * n

        max_right = arr[-1]
        for i in range(-2, -n-1, -1):
            ans[i] = max_right
            max_right = max(max_right, arr[i])

        return ans