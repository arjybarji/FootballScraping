
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
    
    cornerTeams = open("cornersTeams.txt","w",encoding="utf8")
    cornerTeams.write("Corner Teams"+"\n")
    cornerTeamsDict = dict()
    cornerTeamsList = []

    for c in content:
        statsSplit = c.split(",")
        homeTeam = statsSplit[0]
        awayTeam = statsSplit[1]
        corners = statsSplit[-3]
        if(homeTeam not in cornerTeamsDict and homeTeam in teamsL):
            cornerTeamsDict.update({homeTeam : "y"})
        if(awayTeam not in cornerTeamsDict and awayTeam in teamsL):
            cornerTeamsDict.update({awayTeam : "y"})
        if(corners == "-1"):
            cornerTeamsDict.update({homeTeam : "n"})
            cornerTeamsDict.update({awayTeam : "n"})        

    for c in cornerTeamsDict:
        if(cornerTeamsDict[c]=="y"):
            #print(c + ":" + str(cornerTeamsDict[c]))
            cornerTeams.write(c + "\n")

    cornerTeams = open("cornersTeams.txt","w",encoding="utf8")

    cornerTeamsDict = dict()
    cornerTeamsList = []

    cardTeams = open("cardsTeams.txt","w",encoding="utf8")
    cardTeams.write("Card Teams"+"\n")
    cardTeamsDict = dict()
    cardTeamsList = []

    for c in content:
        statsSplit = c.split(",")
        homeTeam = statsSplit[0]
        awayTeam = statsSplit[1]
        cards = statsSplit[19]
        if(homeTeam not in cardTeamsDict and homeTeam in teamsL):
            cardTeamsDict.update({homeTeam : "y"})
        if(awayTeam not in cardTeamsDict and awayTeam in teamsL):
            cardTeamsDict.update({awayTeam : "y"})
        if(cards == "-1"and homeTeam in teamsL and awayTeam in teamsL):
            cardTeamsDict.update({homeTeam : "n"})
            cardTeamsDict.update({awayTeam : "n"})        

    for c in cardTeamsDict:
        if(cardTeamsDict[c]=="y"):
            #print(c + ":" + str(cardTeamsDict[c]))
            cardTeams.write(c + "\n")
