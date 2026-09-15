class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])

        count = [[0] *n for _ in range(26)]

        for vote in votes:
            for pos, team in enumerate(vote):
                count[ord(team) - ord('A')][pos] +=1
        team = votes[0]

        return ''.join(sorted(team,key=lambda team: (*[-x for x in count[ord(team) - ord('A')]],team)))