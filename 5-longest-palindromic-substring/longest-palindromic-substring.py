class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = ""
        def expand(l,r):
            while l>=0 and r< len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return s[l+1:r]

        for i in range(len(s)):
            odd = expand(i,i)
            

            even = expand(i, i+1)

            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even

        return longest








        # def palindrome(substring):
        #     length = len(substring)
        #     if length%2 == 0: #even
        #         l,r = 0, length -1
        #         while l<r:
        #             if substring[l]!=substring[r]:
        #                 return False
        #             l+=1
        #             r-=1
        #         return True

        #     elif length%2 != 0: #odd
        #         l,r = 0, length - 1
        #         while l<r:
        #             if substring[l]!=substring[r]:
        #                 return False
        #             l+=1
        #             r-=1
        #         return True
        #     else:
        #         return False

        # longest = 0
        # l = 0
        # for r, c in enumerate(s):
        #     substring = s[l:r+1]
        #     if palindrome(substring):
        #         longest = max(longest, len(substring))
        #     if not palindrome(substring):
        #         if palindrome(s[l+1:r+1]):
        #             substring = s[l+1:r+1]
        #         elif palindrome(s[l:r+2]):
        #             substring = s[l:r+2]
        # return substring