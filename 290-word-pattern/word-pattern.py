class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        sett = {}
        used_words = set()

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in sett:
                if sett[char] != word:
                    return False
            else:
                if word in used_words:
                    return False
                sett[char] = word
                used_words.add(word)

        return True
