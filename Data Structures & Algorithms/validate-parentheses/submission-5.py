class Solution:
    def isValid(self, s: str) -> bool:
        # no look ---> self 
        stack =  []
        OpenToClose = { ")": "(",  "}": "{",  "]": "["   }

        for c in s:
            if c in OpenToClose:
                if stack and stack[-1] == OpenToClose[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return stack == []