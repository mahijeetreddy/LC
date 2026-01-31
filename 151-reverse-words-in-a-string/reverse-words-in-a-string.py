class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        word = ""
        for c in range(len(s)-1, -1, -1):
            if s[c] != " ":
                word = s[c] + word
            else:
                if word:
                    res.append(word)
                    word = ""
        if word:
            res.append(word)
        return " ".join(res)

