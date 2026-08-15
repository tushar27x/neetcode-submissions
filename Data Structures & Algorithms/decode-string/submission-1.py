class Solution:
    def decodeString(self, s: str) -> str:
        char_stk = []
        num_stk = []
        curr_str = ""
        curr_num = 0
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                num_stk.append(curr_num)
                char_stk.append(curr_str)
                curr_str = ""
                curr_num = 0
            elif c == ']':
                rep = num_stk.pop()
                prev_str = char_stk.pop()
                curr_str = prev_str + curr_str * rep
            else:
                curr_str += c
        
        return curr_str