class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        main = {']':'[', '}':'{', ')':'('}
        stack = deque()
        if len(s)<2:
            return False
        if s[0] in main.keys():
            return False
        for a in s:
            if a in main.keys():
                if stack and stack[-1] == main[a]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(a)
        return True if not stack else False
            
            
            
        