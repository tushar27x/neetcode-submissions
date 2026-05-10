class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk: list[int] = []
        for c in tokens:
            if c == "+":
                second = stk.pop()
                first = stk.pop()
                ans = first + second
                stk.append(ans)
            elif c == "-":
                second = stk.pop()
                first = stk.pop()
                ans = first - second
                stk.append(ans)
            elif c == "/":
                second = stk.pop()
                first = stk.pop()
                ans = int(first / second)
                stk.append(ans)
            elif c == "*":
                second = stk.pop()
                first = stk.pop()
                ans = first * second
                stk.append(ans)
            else :
                stk.append(int(c))
        
        return stk.pop()
        