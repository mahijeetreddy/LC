class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkpal(subs):
            if subs == subs[::-1]:
                return True
        result = 0

        for i in range(len(s)):
            for j in range(i,len(s)):
                substringx = s[i:j+1]
                if checkpal(substringx):
                    result+=1
        return result