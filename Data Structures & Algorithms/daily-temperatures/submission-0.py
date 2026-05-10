class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n: int = len(temperatures)
        ans: list[int] = [0] * n
        stk: list[int] = []

        for i,t in enumerate(temperatures):
            while len(stk) != 0 and t > temperatures[stk[-1]]:
                idx = stk.pop()
                ans[idx] = i - idx
            
            stk.append(i)

        return ans; 