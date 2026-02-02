class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stackS = []
        stackT = []
        for c in s:
            if  c == "#":
                if stackS:
                    stackS.pop()
            else:
                stackS.append(c)
            

        for c in t:
            if  c == "#":
                if stackT:
                    stackT.pop()
            else:
                stackT.append(c)

        if stackS == stackT:
            return True
        else:
            return False