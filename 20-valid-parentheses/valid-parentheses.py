class Solution:
    def isValid(self, s: str) -> bool:
        cto = {
            "}":"{",
            "]":"[",
            ")":"("
        }
        stack = []
        for c in s:
            if c in cto:
                if stack and cto[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack