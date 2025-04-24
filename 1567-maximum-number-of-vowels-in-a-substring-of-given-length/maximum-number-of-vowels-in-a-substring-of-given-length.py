class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # res = 0
        # for i in range(len(s)-k+1):
        #     subs = s[i:i+k]
        #     count = 0
        #     for j in subs:
        #         if j in 'aeiou':
        #             count+=1
        #     res = max(res, count)
        # return res
       
        vowels = 'aeiou'
        mc = count = 0

        for i in range(k):
            if s[i] in vowels:
                count+= 1
        mc = count

        for i in range(k, len(s)):
            if s[i] in vowels:
                count +=1
            if s[i-k] in vowels:
                count-=1
            mc = max(mc, count)

        return mc

