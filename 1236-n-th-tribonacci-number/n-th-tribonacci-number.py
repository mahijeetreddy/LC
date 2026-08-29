class Solution:
    def tribonacci(self, n: int) -> int:
        tn = [0,1,1]

        for i in range(n-2):
            tn.append(tn[i] + tn[i+1] + tn[i+2])
        return tn[n]