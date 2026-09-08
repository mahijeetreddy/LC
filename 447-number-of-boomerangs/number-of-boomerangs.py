class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0

        for i in range(len(points)):
            dist = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]

                distance = dx*dx + dy*dy
                dist[distance]+=1
            for count in dist.values():
                res += count*(count-1)
        return res