class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stackk = []
        for i in operations:
            if i == "C":
                stackk.pop()
            elif i == "D":
                stackk.append(2*stackk[-1])
            elif i == "+":
                stackk.append(stackk[-1] + stackk[-2])
            else:
                stackk.append(int(i))

        return sum(stackk)