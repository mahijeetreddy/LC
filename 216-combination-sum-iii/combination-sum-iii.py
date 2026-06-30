class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if len(cur) == k:
                if total == n:
                    res.append(cur.copy())
                return

            if total>n:
                return
            for num in range(i, 10):
                cur.append(num)
                dfs(num+1, cur , total + num)
                cur.pop()
        dfs(1,[],0)
        return res