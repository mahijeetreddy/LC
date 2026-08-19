class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        satisfied = 0
        extra = 0
        for i in range(n):
            if grumpy[i] == 0:
                satisfied += customers[i]
            elif i< minutes:
                extra += customers[i]
        max_extra = extra
        for i in range(minutes, n):
            outgoing = i - minutes
            if grumpy[outgoing] == 1:
                extra -= customers[outgoing]
            if grumpy[i] == 1:
                extra+= customers[i]
            max_extra = max(max_extra, extra)
        return satisfied + max_extra