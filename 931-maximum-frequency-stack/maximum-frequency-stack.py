from collections import Counter
class FreqStack:

    def __init__(self):
        self.stacks = {}
        self.cnt = Counter()
        self.maxCnt = 0

    def push(self, val: int) -> None:
        self.cnt[val] +=1
        valCnt = self.cnt[val]
        if valCnt> self.maxCnt:
            self.maxCnt = valCnt
            self.stacks[valCnt] = []
        self.stacks[valCnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -=1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -=1
        return res