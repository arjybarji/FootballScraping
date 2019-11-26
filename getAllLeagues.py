with open('fixturesv2.csv',encoding="utf8") as f:
    fixtures = f.readlines()
fixtures = [x.strip() for x in fixtures]

allLeagues = open("leagues.txt","w",encoding="utf8")
leagues = []
for c in fixtures:
    league = c.split(",")[-2]
    if(league not in leagues):
        allLeagues.write(league + "," +"\n")
        leagues.append(league)
        