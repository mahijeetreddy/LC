class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern)!= len(words):
            return False

        pToW = {}
        wToP = {}

        for p,w in zip(pattern, words):
            if p in pToW and pToW[p]!= w:
                return False
            if w in wToP and wToP[w]!= p:
                return False

            pToW[p] = w
            
            wToP[w] = p
            
        return True