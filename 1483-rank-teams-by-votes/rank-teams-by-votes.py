class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        number_of_teams = len(votes[0])

        count = {}

        for team in votes[0]:
            count[team] = [0] * number_of_teams
        
        for vote in votes:
            for position in range(number_of_teams):
                team = vote[position]
                count[team][position] +=1
        
        teams = list(votes[0])

        def sorting_key(team):
            votecounts = []
            for position in count[team]:
                votecounts.append(-position)
            
            return (votecounts, team)
        teams.sort(key = sorting_key)

        return "".join(teams)