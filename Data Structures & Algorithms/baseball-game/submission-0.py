class Solution:
    def is_int(self, s:str) -> bool:
        try:
            int(s)
            return True
        except ValueError:
            return False

    def calPoints(self, operations: List[str]) -> int:
        stk = []
        for op in operations:
            if self.is_int(op):
                stk.append(int(op))
            elif op == "+":
                val1 = stk[-1]
                val2 = stk[-2]
                s = val1 + val2
                stk.append(s)
            elif op == 'D':
                val = stk[-1]
                val *= 2
                stk.append(val)
            elif op == 'C':
                stk.pop()
        
        score = 0
        while stk:
            score += stk.pop()
        
        return score