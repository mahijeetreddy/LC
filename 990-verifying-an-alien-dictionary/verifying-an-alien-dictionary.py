class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapp = {}

        for i, o in enumerate(order):
            mapp[o] = i

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            for k in range(min(len(word1), len(word2))):
                if word1[k] == word2[k]:
                    continue
                if mapp[word1[k]] > mapp[word2[k]]:
                    return False
                break
            else:
                if len(word1) > len(word2):
                    return False
        return True