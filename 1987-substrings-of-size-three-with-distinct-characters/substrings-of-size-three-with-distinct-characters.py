class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        output = 0
        def helper(s):
            seen = set()
            for c in s:
                if c in seen:
                    return False
                seen.add(c)
            return True
        for i in range(0, len(s) -3+1):
            if helper(s[i:i+3]):
                output+=1
        return output