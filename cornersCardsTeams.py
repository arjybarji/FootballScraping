
def cornersCardsTeamsx():
    with open('Statsv2.csv',encoding="utf8") as f:
        content = f.readlines()
    content = [x.strip() for x in content]

    with open('fixturesv2.csv',encoding="utf8") as f:
        fixtures = f.readlines()
    fixtures = [x.strip() for x in fixtures]

    teamsL = []
    teams = open("teams.txt","w",encoding="utf8")
    teams.write("Teams" + "\n")

    cornerTeams = open("cornersTeams.txt","w",encoding="utf8")

    cornerTeamsDict = dict()
    cornerTeamsList = []

    for c in content:
        statsSplit = c.split(",")
        homeTeam = statsSplit[0]
        awayTeam = statsSplit[1]
        corners = statsSplit[-3]
        if(homeTeam not in cornerTeamsDict):
            cornerTeamsDict.update({homeTeam : 0})
        if(awayTeam not in cornerTeamsDict):
            cornerTeamsDict.update({awayTeam : 0})
        if(corners == "-1"):
            cornerTeamsDict.update({homeTeam : cornerTeamsDict[homeTeam]+1})
            cornerTeamsDict.update({awayTeam : cornerTeamsDict[awayTeam]+1})        

    for c in cornerTeamsDict:
        if(cornerTeamsDict[c]<1):
            #print(c + ":" + str(cornerTeamsDict[c]))
            cornerTeams.write(c + "\n")

    cornerTeams = open("cornersTeams.txt","w",encoding="utf8")

    cornerTeamsDict = dict()
    cornerTeamsList = []

    cardTeams = open("cardsTeams.txt","w",encoding="utf8")

    cardTeamsDict = dict()
    cardTeamsList = []

    for c in content:
        statsSplit = c.split(",")
        homeTeam = statsSplit[0]
        awayTeam = statsSplit[1]
        cards = statsSplit[19]
        if(homeTeam not in cardTeamsDict):
            cardTeamsDict.update({homeTeam : 0})
        if(awayTeam not in cardTeamsDict):
            cardTeamsDict.update({awayTeam : 0})
        if(cards == "-1"):
            cardTeamsDict.update({homeTeam : cardTeamsDict[homeTeam]+1})
            cardTeamsDict.update({awayTeam : cardTeamsDict[awayTeam]+1})        

    for c in cardTeamsDict:
        if(cardTeamsDict[c]<1):
            #print(c + ":" + str(cardTeamsDict[c]))
            cardTeams.write(c + "\n")

    for c in fixtures:
        statsSplit = c.split(",")
        homeTeam = statsSplit[0]
        awayTeam = statsSplit[1]
        if(homeTeam not in teamsL): 
            teamsL.append(homeTeam)
            teams.write(homeTeam + "\n")
        if(awayTeam not in teamsL): 
            teamsL.append(awayTeam)
            teams.write(awayTeam + "\n")
    print(teamsL)