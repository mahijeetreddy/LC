class Solution:
    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        l,r = 0, n-1

        for i in range(n//2):
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1