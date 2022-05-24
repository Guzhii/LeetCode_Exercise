from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = deque()
        stack.append(-1)
        res = 0
        
        for i in range(len(s)):
            e = s[i]
            if e == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    print(stack[0])
                    res = max(res, i-stack[-1])
                
        return res
