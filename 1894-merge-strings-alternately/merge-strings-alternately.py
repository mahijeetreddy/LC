class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = []
        if len(word1) >len(word2):
            diff = word1[len(word2):]
        else:
            diff = word2[len(word1):]
        for i in range(min(len(word1), len(word2))):
            new.append(word1[i])
            new.append(word2[i])
        newword = "".join(new)
        newword = newword + diff
        return newword
