class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        mem = [[None] * (n+1) for _ in range(n)]

        def backtrack(i, balance):
            if balance < 0:
                return False

            if i == len(s):
                return balance == 0

            if mem[i][balance] is not None:
                return mem[i][balance]
            
            if s[i] == '(':
                result = backtrack(i+1, balance+1)
            elif s[i] == ')':
                result = backtrack(i+1, balance-1)
            else:
                result = (
                    backtrack(i+1, balance-1) or
                    backtrack(i+1, balance+1) or 
                    backtrack(i+1, balance)
                )
            
            mem[i][balance] = result
            return result

        return backtrack(0,0)