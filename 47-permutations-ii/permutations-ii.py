class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = Counter(nums)

        def dfs():
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n] >0:
                    count[n]-=1
                    perm.append(n)
                    dfs()
                    count[n]+=1
                    perm.pop()
        dfs()
        return res