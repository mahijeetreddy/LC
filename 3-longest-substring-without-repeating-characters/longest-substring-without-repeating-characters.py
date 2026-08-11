from collections import Counter
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right, c in enumerate(s):
            while c in seen:
                seen.remove(s[left])
                left+=1
            
            seen.add(c)
            longest  = max(longest, right - left +1)
        return longest