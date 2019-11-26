import sqlite3
import datetime
import time
import winsound

def insertIntoDatabase():
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    with open('Statsv2.csv',encoding="utf8") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    cursor = conn.cursor()
    for c in content:
        statsSplit = c.split(",")
        cursor.execute("SELECT * FROM stats WHERE gameID = ?", (statsSplit[-1],))
        data=cursor.fetchall()
        if(len(data)==0):
            print("Inserting " + statsSplit[0] + " vs " + statsSplit[1])
            cursor.execute("INSERT INTO stats(homeTeam,awayTeam,gameWeek,homeGoals,awayGoals,matchGoals,BTTS,firstHalfHomeGoals,firstHalfHomeConc,firstHalfAwayGoals,firstHalfAwayConc,firstHalfTotalGoals,secondHalfHomeGoals,secondHalfHomeConc,secondHalfAwayGoals,secondHalfAwayConc,secondHalfTotalGoals,homeTeamCards,awayTeamCards,matchCards,homeCorners,awayCorners,homeCornersConc,awayCornersConc,matchCorners,league,gameID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(statsSplit[0],statsSplit[1],statsSplit[2],int(statsSplit[3]),int(statsSplit[4]),int(statsSplit[5]),statsSplit[6],int(statsSplit[7]),int(statsSplit[8]),int(statsSplit[9]),int(statsSplit[10]),int(statsSplit[11]),int(statsSplit[12]),int(statsSplit[13]),int(statsSplit[14]),int(statsSplit[15]),int(statsSplit[16]),int(statsSplit[17]),int(statsSplit[18]),int(statsSplit[19]),int(statsSplit[20]),int(statsSplit[21]),int(statsSplit[22]),int(statsSplit[23]),int(statsSplit[24]),statsSplit[25],int(statsSplit[26]),))
    conn.commit()
    cursor.close()
    conn.close()
    
    
def asianCardHandicap(homeTeam,awayTeam,date,league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT AVG(homeTeamCards) FROM stats WHERE homeTeam = ?", (homeTeam,))
    homeTeamHomeCards=cursor.fetchall()[0][0]
    cursor.execute("SELECT AVG(awayTeamCards) FROM stats WHERE awayTeam = ?", (homeTeam,))
    homeTeamAwayCards=cursor.fetchall()[0][0]
    homeTotalTeamCards = (homeTeamHomeCards + homeTeamAwayCards)/2
    
    cursor.execute("SELECT AVG(homeTeamCards) FROM stats WHERE homeTeam = ?", (awayTeam,))
    awayTeamHomeCards=cursor.fetchall()[0][0]
    cursor.execute("SELECT AVG(awayTeamCards) FROM stats WHERE awayTeam = ?", (awayTeam,))
    awayTeamAwayCards=cursor.fetchall()[0][0]
    awayTotalTeamCards = (awayTeamHomeCards + awayTeamAwayCards)/2
    
    if((homeTeamHomeCards-awayTeamAwayCards)>=1 and (homeTotalTeamCards-awayTotalTeamCards)>=1):
        print(homeTeam + " vs " + awayTeam)
        bets.write(date + "," +homeTeam +",0.0 Asian Card Handicap," +  league + "\n")
    if((awayTeamAwayCards-homeTeamHomeCards)>=1 and (awayTotalTeamCards-homeTotalTeamCards)>=1):
        print(homeTeam + " vs " + awayTeam)
        bets.write(date + "," +awayTeam +",0.0 Asian Card Handicap," +  league + "\n")
    
def cornerMatchBet(homeTeam,awayTeam,date,league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT AVG(homeCorners) FROM stats WHERE homeTeam = ?", (homeTeam,))
    homeTeamHomeCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT AVG(awayCorners) FROM stats WHERE awayTeam = ?", (homeTeam,))
    homeTeamAwayCorners=cursor.fetchall()[0][0]
    homeTotalTeamCorners = (homeTeamHomeCorners + homeTeamAwayCorners)/2
    
    cursor.execute("SELECT AVG(homeCorners) FROM stats WHERE homeTeam = ?", (awayTeam,))
    awayTeamHomeCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT AVG(awayCorners) FROM stats WHERE awayTeam = ?", (awayTeam,))
    awayTeamAwayCorners=cursor.fetchall()[0][0]
    awayTotalTeamCorners = (awayTeamHomeCorners + awayTeamAwayCorners)/2
    
    if((homeTeamHomeCorners-awayTeamAwayCorners)>=2 and (homeTotalTeamCorners-awayTotalTeamCorners)>=2):
        print(homeTeam + " vs " + awayTeam)
        bets.write(date + "," +homeTeam + ",Corner Match Bet," +  league + "\n")
    if((awayTeamAwayCorners-homeTeamHomeCorners)>=2 and (awayTotalTeamCorners-homeTotalTeamCorners)>=2):
        print(homeTeam + " vs " + awayTeam)
        bets.write(date + "," +awayTeam + ",Corner Match Bet," +  league + "\n")
        
def teamCards(homeTeam,awayTeam,date,league,num):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(homeTeamCards) FROM stats WHERE homeTeam = ? AND homeTeamCards >"+num, (homeTeam,))
    homeTeamCountHomeCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(homeTeamCards ) FROM stats WHERE homeTeam = ?", (homeTeam,))
    homeTeamHomeGames=cursor.fetchall()[0][0]
    homeTeamPercentHome = homeTeamCountHomeCorners/homeTeamHomeGames
    
    cursor.execute("SELECT COUNT(awayTeamCards) FROM stats WHERE awayTeam = ? AND awayTeamCards > "+num, (homeTeam,))
    homeTeamCountAwayCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(awayTeamCards) FROM stats WHERE awayTeam = ?", (homeTeam,))
    homeTeamAwayGames=cursor.fetchall()[0][0]
    homeTeamTotalCount = homeTeamHomeGames  + homeTeamAwayGames
    homeTeamTotalCornerCount = homeTeamCountHomeCorners + homeTeamCountAwayCorners
    homeTeamPercentTotal = homeTeamTotalCornerCount/homeTeamTotalCount
    
    if(homeTeamPercentHome > .85 and homeTeamPercentTotal > .85):
        print(homeTeam)
        bets.write(date + "," +homeTeam + ",Over "+str(int(float(num)-0.5))+" Team Cards," +  league + "\n")
    if(homeTeamPercentHome < .15 and homeTeamPercentTotal < .15):
        print(homeTeam)
        bets.write(date + "," +homeTeam + ",Under "+str(int(float(num)+0.5))+" Team Cards," +  league + "\n")
    
    cursor.execute("SELECT COUNT(awayTeamCards) FROM stats WHERE awayTeam = ? AND awayTeamCards >"+num, (awayTeam,))
    awayTeamCountHomeCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(awayTeamCards ) FROM stats WHERE awayTeam = ?", (awayTeam,))
    awayTeamHomeGames=cursor.fetchall()[0][0]
    awayTeamPercentHome = awayTeamCountHomeCorners/awayTeamHomeGames
    
    cursor.execute("SELECT COUNT(homeTeamCards) FROM stats WHERE homeTeam = ? AND homeTeamCards >"+num, (awayTeam,))
    awayTeamCountAwayCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(homeTeamCards) FROM stats WHERE homeTeam = ?", (awayTeam,))
    awayTeamAwayGames=cursor.fetchall()[0][0]
    awayTeamTotalCount = awayTeamHomeGames  + awayTeamAwayGames
    awayTeamTotalCornerCount = awayTeamCountHomeCorners + awayTeamCountAwayCorners
    awayTeamPercentTotal = awayTeamTotalCornerCount/awayTeamTotalCount
    
    if(awayTeamPercentHome > .85 and awayTeamPercentTotal > .85):
        print(awayTeam)
        bets.write(date + "," + awayTeam + ",Over "+str(int(float(num)-0.5))+" Team Cards," + league + "\n")
    if(awayTeamPercentHome < .15 and awayTeamPercentTotal < .15):
        print(awayTeam)
        bets.write(date + "," + awayTeam + ",Under "+str(int(float(num)+0.5))+" Team Cards," + league + "\n")

def teamCorners(homeTeam,awayTeam,date,league,num):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(homeCorners) FROM stats WHERE homeTeam = ? AND homeCorners > "+num, (homeTeam,))
    homeTeamCountHomeCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(homeCorners ) FROM stats WHERE homeTeam = ?", (homeTeam,))
    homeTeamHomeGames=cursor.fetchall()[0][0]
    homeTeamPercentHome = homeTeamCountHomeCorners/homeTeamHomeGames
    
    cursor.execute("SELECT COUNT(awayCorners) FROM stats WHERE awayTeam = ? AND awayCorners > "+num, (homeTeam,))
    homeTeamCountAwayCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(awayCorners) FROM stats WHERE awayTeam = ?", (homeTeam,))
    homeTeamAwayGames=cursor.fetchall()[0][0]
    homeTeamTotalCount = homeTeamHomeGames  + homeTeamAwayGames
    homeTeamTotalCornerCount = homeTeamCountHomeCorners + homeTeamCountAwayCorners
    homeTeamPercentTotal = homeTeamTotalCornerCount/homeTeamTotalCount
    
    if(homeTeamPercentHome > .9 and homeTeamPercentTotal > .9):
        print(homeTeam)
        bets.write(date + "," +homeTeam + ",Over "+str(int(float(num)-0.5))+" Team Corners," + league + "\n")
    if(homeTeamPercentHome < .1 and homeTeamPercentTotal < .1):
        print(homeTeam)
        bets.write(date + "," +homeTeam + ",Under "+str(int(float(num)-0.5))+" Team Corners," + league + "\n")
    
    cursor.execute("SELECT COUNT(awayCorners) FROM stats WHERE awayTeam = ? AND awayCorners > "+num, (awayTeam,))
    awayTeamCountHomeCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(awayCorners ) FROM stats WHERE awayTeam = ?", (awayTeam,))
    awayTeamHomeGames=cursor.fetchall()[0][0]
    awayTeamPercentHome = awayTeamCountHomeCorners/awayTeamHomeGames
    
    cursor.execute("SELECT COUNT(homeCorners) FROM stats WHERE homeTeam = ? AND homeCorners > "+num, (awayTeam,))
    awayTeamCountAwayCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(homeCorners) FROM stats WHERE homeTeam = ?", (awayTeam,))
    awayTeamAwayGames=cursor.fetchall()[0][0]
    awayTeamTotalCount = awayTeamHomeGames  + awayTeamAwayGames
    awayTeamTotalCornerCount = awayTeamCountHomeCorners + awayTeamCountAwayCorners
    awayTeamPercentTotal = awayTeamTotalCornerCount/awayTeamTotalCount
    
    if(awayTeamPercentHome > .85 and awayTeamPercentTotal > .85):
        print(awayTeam)
        bets.write(date + "," +awayTeam + ",Over "+str(int(float(num)-0.5))+" Team Corners," +league + "\n")
    if(awayTeamPercentHome < .15 and awayTeamPercentTotal < .15):
        print(awayTeam)
        bets.write(date + "," +awayTeam + ",Under "+str(int(float(num)-0.5))+" Team Corners," + league + "\n")   

def checkAvgGoals(homeTeam,awayTeam,field,lower,upper,bet,date,league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT AVG("+field+") FROM stats WHERE homeTeam = ?", (homeTeam,))
    homeGoals=cursor.fetchall()[0][0]
    cursor.execute("SELECT AVG("+field+") FROM stats WHERE awayTeam = ?", (homeTeam,))
    homeTotalGoals = (homeGoals + cursor.fetchall()[0][0])/2
    
    cursor.execute("SELECT AVG("+field+") FROM stats WHERE awayTeam = ?", (awayTeam,))
    awayGoals=cursor.fetchall()[0][0]
    cursor.execute("SELECT AVG("+field+") FROM stats WHERE homeTeam = ?", (awayTeam,))
    awayTotalGoals = (awayGoals + cursor.fetchall()[0][0])/2

    if(field == "secondHalfTotalGoals"):
        field = "SH Goals"
    if(field == "matchCards"):
        field = "Match Cards"
    if(field == "matchCorners"):
        field = "Corners"
    if(bet == "1"):
        bet = "1.0"
    if(homeGoals <lower) and (awayGoals <lower) and (homeTotalGoals <lower) and (awayTotalGoals <lower):
        if(field != "matchGoals" and field !="SH Goals" and field !="firstHalfTotalGoals"):
            bet = str(int(float(bet)+0.5))
        if(("matchGoals" in field) and ("1.5" in bet)):
            field = "1.5 BET"
        if(field == "matchGoals"):
            field = "Goals"         
        if(field == "firstHalfTotalGoals"):
            field = "FH Goal Line"            
        bets.write(date + "," +homeTeam + " vs " + awayTeam + "," + "Under " +bet + " " + field+"," + league + "\n")
        print("Under "+bet)
    if(homeGoals >upper )and (awayGoals >upper) and (homeTotalGoals >upper) and (awayTotalGoals >upper):
        if(field != "matchGoals" and field !="SH Goals"and field !="firstHalfTotalGoals"):
            bet = str(int(float(bet)-0.5))
        if(("matchGoals" in field) and ("1.5" in bet)):
            field = "1.5 BET"
        if(field == "matchGoals"):
            field = "Goals"
        if(field == "firstHalfTotalGoals"):
            field = "FH Goal Line"   
        bets.write(date + "," +homeTeam + " vs " + awayTeam + "," + "Over " +bet+ " " + field+ "," +league +"\n")
        print("Over "+bet)
    
def teamPercentStats(homeTeam,awayTeam,field,lower,upper,bet,date,league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE homeTeam = ? AND "+field+" > "+bet , (homeTeam,))
    teamHomeOver=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE homeTeam = ?" , (homeTeam,))
    teamHomeCount=cursor.fetchall()[0][0]
    homeTeamHomeOver = teamHomeOver/teamHomeCount
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE awayTeam = ? AND "+field+" > "+bet , (homeTeam,))
    teamAwayOver=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE awayTeam = ?" , (homeTeam,))
    teamAwayCount=cursor.fetchall()[0][0]
    homeTeamTotalOver = (teamHomeOver + teamAwayOver)/(teamHomeCount+teamAwayCount)

    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE awayTeam = ? AND "+field+" > "+bet , (awayTeam,))
    teamAwayOver=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE awayTeam = ?" , (awayTeam,))
    teamAwayCount=cursor.fetchall()[0][0]
    awayTeamAwayOver = teamAwayOver/teamAwayCount
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE homeTeam = ? AND "+field+" > "+bet , (awayTeam,))
    teamHomeOver=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE homeTeam = ?" , (awayTeam,))
    teamHomeCount=cursor.fetchall()[0][0]
    awayTeamTotalOver = (teamHomeOver + teamAwayOver)/(teamHomeCount+teamAwayCount) 
    
    
    if(field == "firstHalfTotalGoals"):
        field = "FH Goal Line"
    if(field == "secondHalfTotalGoals"):
        field = "SH Goals"
    if(field == "matchCards"):
        field = "Match Cards"
    if(field == "matchCorners"):
        field = "Corners"
    if(bet == "1"):
        bet = "1.0"

    if(homeTeamHomeOver <lower) and (awayTeamAwayOver <lower) and (homeTeamTotalOver <lower) and (awayTeamTotalOver <lower):
        if(field != "matchGoals" and field !="SH Goals"):
            bet = str(int(float(bet)+0.5))
            
        if(("matchGoals" in field) and ("1.5" in bet)):
            field = "1.5 BET"
        if(field == "matchGoals"):
            field = "Goals"
        bets.write(date + "," +homeTeam + " vs " + awayTeam + ","  + "Under " +bet + " " + field + "," + league + "\n")
        print("Under "+bet)
    if(homeTeamHomeOver >upper )and (awayTeamAwayOver >upper) and (homeTeamTotalOver >upper) and (awayTeamTotalOver >upper):
        if(field != "matchGoals" and field !="SH Goals"):
            bet = str(int(float(bet)-0.5))
            if(int(bet) == 0):
                bet = "1.0"
        if(("matchGoals" in field) and ("1.5" in bet)):
            field = "1.5 BET"
        if(field == "matchGoals"):
            field = "Goals"
        if(field == "FH Goal Line" and bet == 2.0):
            bet = "1.0,1.5"
        bets.write(date + "," +homeTeam + " vs " + awayTeam + "," + "Over " +bet+ " " + field+ "," +league + "\n")
        print("Over "+bet)

def BTTSStats(homeTeam,awayTeam,field,lower,upper,date,league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE homeTeam = ? AND "+field+" = 'y'" , (homeTeam,))
    homeBTTSHome = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE homeTeam = ?" , (homeTeam,))
    homeBTTSHomeCount = cursor.fetchall()[0][0]
    homeBTTSHomePercent = homeBTTSHome/homeBTTSHomeCount
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE awayTeam = ? AND "+field+" = 'y'" , (homeTeam,))
    homeBTTSAway = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE awayTeam = ?" , (homeTeam,))
    homeBTTSAwayCount = cursor.fetchall()[0][0]
    homeBTTSTotal = (homeBTTSHome + homeBTTSAway)/(homeBTTSHomeCount+homeBTTSAwayCount)

    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE awayTeam = ? AND "+field+" = 'y'" , (awayTeam,))
    awayBTTSAway = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE awayTeam = ?" , (awayTeam,))
    awayBTTSAwayCount = cursor.fetchall()[0][0]
    awayBTTSAwayPercent = awayBTTSAway/awayBTTSAwayCount
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE homeTeam = ? AND "+field+" = 'y'" , (awayTeam,))
    awayBTTSHome = cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT("+field+") FROM stats WHERE homeTeam = ?" , (awayTeam,))
    awayBTTSHomeCount = cursor.fetchall()[0][0]
    awayBTTSTotal = (awayBTTSAway + awayBTTSHome)/(awayBTTSAwayCount+awayBTTSHomeCount)
    
    if(homeBTTSHomePercent < lower) and (homeBTTSTotal < lower) and (awayBTTSAwayPercent < lower) and (awayBTTSTotal < lower):
        print("BTTS No")
        bets.write(date + "," +homeTeam + " vs " + awayTeam + ","+field.upper()+" No"+ "," + league +"\n")
    if(homeBTTSHomePercent >upper) and (homeBTTSTotal >upper) and (awayBTTSAwayPercent >upper) and (awayBTTSTotal >upper):
        print("BTTS Yes")
        bets.write(date + "," +homeTeam + " vs " + awayTeam+field.upper()+" Yes" + ","+ league +"\n")

def predict(homeTeam,awayTeam,gameweek,date,league):

    print(homeTeam + "," + awayTeam + "," + date)
    checkAvgGoals(homeTeam,awayTeam,"matchGoals",1.8,3.2,"2.5",date,league)
    checkAvgGoals(homeTeam,awayTeam,"firstHalfTotalGoals",0.65,1.35,"1.0",date,league)
    checkAvgGoals(homeTeam,awayTeam,"secondHalfTotalGoals",0.8,2.2,"1.5",date,league) 
    
    teamPercentStats(homeTeam,awayTeam,"matchGoals",0.25,0.75,"2.5",date,league)
    teamPercentStats(homeTeam,awayTeam,"matchGoals",0.1,0.89,"1.5",date,league)
    #teamPercentStats(homeTeam,awayTeam,"matchGoals",0.25,0.75,"3.5",date,league)
    teamPercentStats(homeTeam,awayTeam,"firstHalfTotalGoals",0.2,0.8,"0.5",date,league)
    teamPercentStats(homeTeam,awayTeam,"firstHalfTotalGoals",0.2,0.8,"0.5",date,league)
    teamPercentStats(homeTeam,awayTeam,"secondHalfTotalGoals",0.2,0.8,"1.5",date,league)
    
    BTTSStats(homeTeam,awayTeam,"btts",0.2,0.8,date,league)
    
    if((homeTeam in cardsTeams) and (awayTeam in cardsTeams) and (league != "National League CHANGE")):
        #Asian Card Handicap Averages
            #If team1 has 1 cards less than 2 avg H/A and Total
        asianCardHandicap(homeTeam,awayTeam,date,league)
        
        #Over/Under 4.5 Cards Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCards",0.2,0.8,"3.5",date,league)
        #Over/Under 5.5 Cards Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCards",0.2,0.8,"4.5",date,league)        
        #Over/Under 1.5 Team Cards H/A and Total
        teamCards(homeTeam,awayTeam,date,league,"1.5")
    if((homeTeam in cornersTeams) and (awayTeam in cornersTeams)):    
        #Over/Under 8 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.2,0.8,"8.5",date,league)
        #Over/Under 10 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.2,0.8,"9.5",date,league)
        #Over/Under 10 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.2,0.8,"10.5",date,league)
        #Over/Under 10 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.2,0.8,"11.5",date,league)
        #Over/Under 10 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.2,0.8,"12.5",date,league)
        
        #Over/Under 4.5 Corners Percent 80/20 H/A and Total
        teamCorners(homeTeam,awayTeam,date,league,"3.5")
        
        #Corner Match Bet
            #If Team1 has 2 Less than Team2 Taken vs Conc H/A and Total
            #So City have 5.5 Avg Taken Home and 5.6 Taken Total where West Ham have 3.4 Taken Home and 3.5 Taken Total. City have Corner Match Bet
        cornerMatchBet(homeTeam,awayTeam,date,league)
        
leaguesDict = dict()
if __name__ == '__main__':
    start_time = time.time()
    insertIntoDatabase()
    with open('fixturesv2.csv',encoding="utf8") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    
    with open('cornersTeams.txt',encoding="utf8") as f:
        cornersTeams = f.readlines()
    cornersTeams = [x.strip() for x in cornersTeams]
    
    with open('cardsTeams.txt',encoding="utf8") as f:
        cardsTeams = f.readlines()
    cardsTeams = [x.strip() for x in cardsTeams]
    
    with open('leagueTransform.csv',encoding="utf8") as f:
        leaguesT = f.readlines()
    leaguesT = [x.strip() for x in leaguesT]
    
    for l in leaguesT:
        leaguesDict.update({l.split(",")[0] : l.split(",")[1]})

    bets = open("bets.csv","w",encoding="utf8")
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=30)
    tomorrow = tomorrow.strftime("%B")
    today = today.strftime("%B")
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    for c in content:
        split = c.split(",")
        homeTeam = split[0]
        awayTeam = split[1]
        gameweek = split[2]
        cursor.execute("SELECT COUNT(gameID) FROM stats WHERE homeTeam = ? OR awayTeam = ?", (homeTeam,homeTeam,))
        data=cursor.fetchall()[0][0]
        date = split[3]
        league = leaguesDict[split[4]]
        if(today.lower() in date.lower() and data>7) or (tomorrow.lower() in date.lower() and data>7):
        #if(today.lower() in date.lower() and int(gameweek)>7):
            predict(homeTeam,awayTeam,gameweek,date,league)
    bets.close()
    
    temp = []
    with open('bets.csv',encoding="utf8") as f:
        bets2 = f.readlines()
    bets2 = [x.strip() for x in bets2]
    f.close()
    bets3 = open("bets.csv","w",encoding="utf8")
    one = open("Over2.csv","w",encoding="utf8")
    for b in bets2:
        if("Over 1.5 1.5 BET" in b):
            one.write(b + "\n")
        elif(b not in temp):
            bets3.write(b + "\n")
            temp.append(b)
    
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)        
    print("--- %s minutes ---" % ((time.time() - start_time)/60))
    input("Done")
