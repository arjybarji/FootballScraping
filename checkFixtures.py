with open('fixturesv2.csv',encoding="utf8") as f:
        content = f.readlines()
content = [x.strip() for x in content]

leagues = dict()

for c in content:
    league = c.split(",")[4]
    if(league not in leagues):
        leagues.update({league: 0})
    leagues.update({league : leagues[league]+1})

with open('Statsv2.csv',encoding="utf8") as f:
        content = f.readlines()
content = [x.strip() for x in content]

for c in content:
    league = c.split(",")[25]
    if(league not in leagues):
        leagues.update({league: 0})
    leagues.update({league : leagues[league]+1})
    
for league in leagues:
    print(league + " - " + str(leagues[league]))