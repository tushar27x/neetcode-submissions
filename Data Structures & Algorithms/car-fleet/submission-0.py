class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stk = []

        for pos, speed in cars:
            time = (target - pos) / speed
            stk.append(time)

            if len(stk) >= 2 and stk[-1] <= stk[-2]:
                stk.pop()

        return len(stk)