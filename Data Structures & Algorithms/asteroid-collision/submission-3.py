class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for ast in asteroids:
            while stk and (ast<0 and stk[-1] > 0):
                if abs(ast) > stk[-1]: 
                    stk.pop()
                    continue

                elif abs(ast) == stk[-1]:
                    stk.pop()
                
                break
            
            else:
                stk.append(ast)

        return stk