class Solution:
    def romanToInt(self, s: str) -> int:
        mapp = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000,
        }
        total = 0
        for i in range(len(s)):
            if i+1 < len(s) and mapp[s[i]] < mapp[s[i+1]]:
                total -= mapp[s[i]]
            else:
                total += mapp[s[i]]
        return total