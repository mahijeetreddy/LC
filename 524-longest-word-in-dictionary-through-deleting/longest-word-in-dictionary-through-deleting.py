class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        best = ""
        for word in dictionary:
            i = 0
            j = 0
            while i<len(word) and j< len(s):
                if word[i] == s[j]:
                    i +=1
                j+=1

            if i == len(word):
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best= word
        return best

            

