class Solution:
    def isValid(self, s: str) -> bool:
        stk: list[int] = []
        
        for c in s:
            if c == ")" or c == "]" or c == "}":
                if len(stk) == 0:
                    return False
                elif c == ")" and stk[-1] == "(" :
                    stk.pop()
                elif c == "]" and stk[-1] == "[":
                    stk.pop()
                elif c == "}" and stk[-1] == "{":
                    stk.pop()
                else:
                    return False
            else:
                stk.append(c)
        
        return len(stk) == 0