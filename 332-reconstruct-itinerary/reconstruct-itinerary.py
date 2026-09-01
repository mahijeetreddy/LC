class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        places = defaultdict(list)

        for fro, to in tickets:
            places[fro].append(to)
        for airport in places:
            places[airport].sort(reverse= True)

        def dfs(airport):
            while places[airport]:
                nxt = places[airport].pop()
                dfs(nxt)
            res.append(airport)
        dfs("JFK")
        return res[::-1]