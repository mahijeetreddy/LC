class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        i = j = 0
        while i<n:
            start = i
            while i+1< n and chars[i] == chars[i+1]:
                i+=1
            count = i - start + 1
            chars[j] = chars[i]
            j+=1
            if count>1:
                for val in str(count):
                    chars[j] = val
                    j+=1
            i+=1
        return j