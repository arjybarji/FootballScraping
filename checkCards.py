
with open("Statsv2.csv","r",encoding = "utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content]

nil = open("NoCards.csv","w",encoding = "utf8")

for c in content:
    id = c.split(",")[26]
    matchCards = c.split(",")[19]
    if(matchCards == "0"):
        leagueUrl = 'https://us.soccerway.com/matches/2018/08/10/england/premier-league/manchester-united-fc/leicester-city-fc/'
        nil.write( leagueUrl +id+'/' + "\n")
