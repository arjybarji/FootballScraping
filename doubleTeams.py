with open('fixturesv2.csv',encoding="utf8") as f:
        content = f.readlines()
content = [x.strip() for x in content]

teams = dict()

def dictAdd(team):
    if(team not in teams):
        teams.update({team : league})
    if(team in teams and teams[team] != league):
        print(team)
for c in content:
    homeTeam = c.split(",")[0]
    awayTeam = c.split(",")[1]
    league = c.split(",")[4]
    dictAdd(homeTeam)
    dictAdd(awayTeam)
    