
with open("Statsv2.csv","r",encoding = "utf8") as f:
    Statsv2 = f.readlines()
Statsv2 = [x.strip() for x in Statsv2]
results = open("results.csv","w",encoding="utf8")
cardResults = open("cardHandicap.csv","w",encoding="utf8")

for s in Statsv2:
    result = ""
    splits = s.split(",")
    homeTeam = splits[0]
    awayTeam = splits[1]
    homeGoals = int(splits[3])
    awayGoals = int(splits[4])
    date = splits[2]
    id = splits[-1]
    league = splits[-2]
    if(homeGoals > awayGoals):
        result = homeTeam
    if(homeGoals < awayGoals):
        result = awayTeam
    if(homeGoals == awayGoals):
        result = "draw"
    results.write(homeTeam + "," + awayTeam + "," + result + "," + date + "," + league + "\n")
    
    resultC = ""
    homeCards = int(splits[17])
    awayCards = int(splits[18])
    if(homeCards != -1 or awayCards !=-1):
        if(homeCards > awayCards):
            resultC = homeTeam
        if(homeCards < awayCards):
            resultC = awayTeam
        if(homeCards == awayCards):
            resultC = "draw"
        cardResults.write(homeTeam + "," + awayTeam + "," + resultC + "," + date + "," + league + "\n")