class Solution:
    def countSubstrings(self, s: str) -> int:
        # def checkpal(subs):
        #     if subs == subs[::-1]:
        #         return True
        # result = 0

        # for i in range(len(s)):
        #     for j in range(i,len(s)):
        #         substringx = s[i:j+1]
        #         if checkpal(substringx):
        #             result+=1
        # return result
        result = 0

        def expand(left, right):
            count = 0
            while left>=0 and right< len(s) and s[left] == s[right]:
                count+=1
                left -=1
                right +=1
            return count
        for i in range(len(s)):
            result += expand(i,i)
            result+= expand(i, i+1)

        return result