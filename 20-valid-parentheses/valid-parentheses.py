class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        stack = []

        for c in s:
            if c in mapping:
                if not stack or stack.pop()!= mapping[c]:
                    return False
            else:
                stack.append(c)
        return not stack