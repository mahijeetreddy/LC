class FreqStack:
    def __init__(self):
        self.stacks = defaultdict(list)
        self.cnt = Counter()
        self.maxCnt = 0

    def push(self, val: int) -> None:
        self.cnt[val] +=1
        freq = self.cnt[val]
        self.maxCnt = max(self.maxCnt, freq)
        self.stacks[freq].append(val)

    def pop(self) -> int:
        res = self.stacks[self.maxCnt].pop()
        self.cnt[res] -=1
        if not self.stacks[self.maxCnt]:
            self.maxCnt -=1
        return res