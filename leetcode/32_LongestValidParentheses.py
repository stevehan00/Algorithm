class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stk = []
        maxleft = -1
        
        for i in range(len(s)):
            if s[i] == '(':
                stk.append(i)
            else:
                if stk:
                    stk.pop()
                    
                    if stk:
                        res = max(res, i-stk[-1])
                    else:
                        res = max(res, i-maxleft)
                else:
                    maxleft = i
        
        return res