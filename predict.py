import sqlite3
import datetime


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
        bets.write(homeTeam + "," + awayTeam + "," + homeTeam + " Asian Card Handicap," + date + "," + league + "\n")
    if((awayTeamAwayCards-homeTeamHomeCards)>=1 and (awayTotalTeamCards-homeTotalTeamCards)>=1):
        print(homeTeam + " vs " + awayTeam)
        bets.write(homeTeam + "," + awayTeam + "," + awayTeam + " Asian Card Handicap," + date + "," + league + "\n")
    
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
        bets.write(homeTeam + "," + awayTeam + "," + homeTeam + " Corner Match Bet," + date + "," + league + "\n")
    if((awayTeamAwayCorners-homeTeamHomeCorners)>=2 and (awayTotalTeamCorners-homeTotalTeamCorners)>=2):
        print(homeTeam + " vs " + awayTeam)
        bets.write(homeTeam + "," + awayTeam + "," + awayTeam + " Corner Match Bet," + date + "," + league + "\n")

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

    if(homeTeamHomeOver <lower) and (awayTeamAwayOver <lower) and (homeTeamTotalOver <lower) and (awayTeamTotalOver <lower):
        bets.write(homeTeam + "," + awayTeam + ","  + "Under " +bet +" "+ field +"," + date +"," + league + "\n")
        print("Under "+bet)
    if(homeTeamHomeOver >upper )and (awayTeamAwayOver >upper) and (homeTeamTotalOver >upper) and (awayTeamTotalOver >upper):
        bets.write(homeTeam + "," + awayTeam + ","  + "Over " +bet + " " +field+ "," + date +"," + league + "\n")
        print("Over "+bet)
        
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
    
    if(homeTeamPercentHome > .9 and homeTeamPercentTotal > .9):
        print(homeTeam)
        bets.write(homeTeam + "," + awayTeam + "," + homeTeam + " Over 1.5 Cards," + date + "," + league + "\n")
    
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
    
    if(awayTeamPercentHome > .9 and awayTeamPercentTotal > .9):
        print(awayTeam)
        bets.write(homeTeam + "," + awayTeam + "," + awayTeam + " Over "+num+" Cards," + date + "," + league + "\n")

def teamCorners(homeTeam,awayTeam,date,league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(homeCorners) FROM stats WHERE homeTeam = ? AND homeCorners > 4", (homeTeam,))
    homeTeamCountHomeCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(homeCorners ) FROM stats WHERE homeTeam = ?", (homeTeam,))
    homeTeamHomeGames=cursor.fetchall()[0][0]
    homeTeamPercentHome = homeTeamCountHomeCorners/homeTeamHomeGames
    
    cursor.execute("SELECT COUNT(awayCorners) FROM stats WHERE awayTeam = ? AND awayCorners > 4", (homeTeam,))
    homeTeamCountAwayCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(awayCorners) FROM stats WHERE awayTeam = ?", (homeTeam,))
    homeTeamAwayGames=cursor.fetchall()[0][0]
    homeTeamTotalCount = homeTeamHomeGames  + homeTeamAwayGames
    homeTeamTotalCornerCount = homeTeamCountHomeCorners + homeTeamCountAwayCorners
    homeTeamPercentTotal = homeTeamTotalCornerCount/homeTeamTotalCount
    
    if(homeTeamPercentHome > .9 and homeTeamPercentTotal > .9):
        print(homeTeam)
        bets.write(homeTeam + "," + awayTeam + "," + homeTeam + " Over 1.5 Cards," + date + "," + league + "\n")
    
    cursor.execute("SELECT COUNT(awayCorners) FROM stats WHERE awayTeam = ? AND awayCorners > 4", (awayTeam,))
    awayTeamCountHomeCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(awayCorners ) FROM stats WHERE awayTeam = ?", (awayTeam,))
    awayTeamHomeGames=cursor.fetchall()[0][0]
    awayTeamPercentHome = awayTeamCountHomeCorners/awayTeamHomeGames
    
    cursor.execute("SELECT COUNT(homeCorners) FROM stats WHERE homeTeam = ? AND homeCorners > 4", (awayTeam,))
    awayTeamCountAwayCorners=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(homeCorners) FROM stats WHERE homeTeam = ?", (awayTeam,))
    awayTeamAwayGames=cursor.fetchall()[0][0]
    awayTeamTotalCount = awayTeamHomeGames  + awayTeamAwayGames
    awayTeamTotalCornerCount = awayTeamCountHomeCorners + awayTeamCountAwayCorners
    awayTeamPercentTotal = awayTeamTotalCornerCount/awayTeamTotalCount
    
    if(awayTeamPercentHome > .9 and awayTeamPercentTotal > .9):
        print(awayTeam)
        bets.write(homeTeam + "," + awayTeam + "," + awayTeam + " Over 4 Corners," + date + "," + league + "\n")

    
    

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
    if(homeGoals <lower) and (awayGoals <lower) and (homeTotalGoals <lower) and (awayTotalGoals <lower):
        bets.write(homeTeam + "," + awayTeam + "," + "Under " +bet + " " + field+"," + date + "," + league + "\n")
        print("Under "+bet)
    if(homeGoals >upper )and (awayGoals >upper) and (homeTotalGoals >upper) and (awayTotalGoals >upper):
        bets.write(homeTeam + "," + awayTeam + "," + "Over " +bet+ " " + field+ "," + date + "," + league +"\n")
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
    if(".99" in bet):
        bet = "1"
    if(("matchGoals" in field) and ("1.5" in bet)):
        field = "1.5 BET"
    if(homeTeamHomeOver <lower) and (awayTeamAwayOver <lower) and (homeTeamTotalOver <lower) and (awayTeamTotalOver <lower):
        bets.write(homeTeam + "," + awayTeam + ","  + "Under " +bet + " " + field + "," + date +"," + league + "\n")
        print("Under "+bet)
    if(homeTeamHomeOver >upper )and (awayTeamAwayOver >upper) and (homeTeamTotalOver >upper) and (awayTeamTotalOver >upper):
        bets.write(homeTeam + "," + awayTeam + "," + "Over " +bet+ " " + field+ "," + date +"," + league + "\n")
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
        bets.write(homeTeam + "," + awayTeam + ","+field+" no"+ "," + date + "," + league +"\n")
    if(homeBTTSHomePercent >upper) and (homeBTTSTotal >upper) and (awayBTTSAwayPercent >upper) and (awayBTTSTotal >upper):
        print("BTTS Yes")
        bets.write(homeTeam + "," + awayTeam+field+" yes" + ","+ date + "," + league +"\n")

def predict(homeTeam,awayTeam,gameweek,date,league):
    print(homeTeam + "," + awayTeam + "," + date)
    checkAvgGoals(homeTeam,awayTeam,"matchGoals",1.8,3.2,"2.5",date,league)
    checkAvgGoals(homeTeam,awayTeam,"firstHalfTotalGoals",0.65,1.35,"1.0",date,league)
    checkAvgGoals(homeTeam,awayTeam,"secondHalfTotalGoals",0.8,2.2,"1.5",date,league) 
    teamPercentStats(homeTeam,awayTeam,"matchGoals",0.25,0.75,"2.5",date,league)
    teamPercentStats(homeTeam,awayTeam,"matchGoals",0.1,0.89,"1.5",date,league)
    #teamPercentStats(homeTeam,awayTeam,"matchGoals",0.25,0.75,"3.5",date,league)
    teamPercentStats(homeTeam,awayTeam,"firstHalfTotalGoals ",0.2,0.8,".99",date,league)
    teamPercentStats(homeTeam,awayTeam,"secondHalfTotalGoals ",0.2,0.8,"1.5",date,league)
    BTTSStats(homeTeam,awayTeam,"btts",0.2,0.8,date,league)
    if((homeTeam in cardsTeams) and (awayTeam in cardsTeams) and (league != "National League N / S - England")):
        #Asian Card Handicap Averages
            #If team1 has 1 cards less than 2 avg H/A and Total
        asianCardHandicap(homeTeam,awayTeam,date,league)
        
        #Over/Under 3.5 Cards Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCards",0.2,0.8,"3.5",date,league)
        #Over/Under 4.5 Cards Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCards",0.2,0.8,"4.5",date,league)
        #Over/Under 5.5 Cards Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCards",0.2,0.8,"5.5",date,league)
        
        #Over/Under 1.5 Team Cards H/A and Total
        teamCards(homeTeam,awayTeam,date,league,"1.5")
        teamCards(homeTeam,awayTeam,date,league,"2.5")
    if((homeTeam in cornersTeams) and (awayTeam in cornersTeams)):    
        #Over/Under 8 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.2,0.8,"8",date,league)
        #Over/Under 10 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.2,0.8,"10",date,league)
        #Over/Under 12 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.2,0.8,"12",date,league)
        
        #Over/Under 4.5 Corners Percent 80/20 H/A and Total
        teamCorners(homeTeam,awayTeam,date,league)
        
        #Corner Match Bet
            #If Team1 has 2 Less than Team2 Taken vs Conc H/A and Total
            #So City have 5.5 Avg Taken Home and 5.6 Taken Total where West Ham have 3.4 Taken Home and 3.5 Taken Total. City have Corner Match Bet
        cornerMatchBet(homeTeam,awayTeam,date,league)

if __name__ == '__main__':
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

    bets = open("bets.csv","w",encoding="utf8")
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=30)
    tomorrow = tomorrow.strftime("%B")
    today = today.strftime("%B")
    for c in content:
        split = c.split(",")
        homeTeam = split[0]
        awayTeam = split[1]
        gameweek = split[2]
        date = split[3]
        league = split[4]
        #if(today.lower() in date.lower() and int(gameweek)>7) or (tomorrow.lower() in date.lower() and int(gameweek)>7):
        if(today.lower() in date.lower() and int(gameweek)>7):
            predict(homeTeam,awayTeam,gameweek,date,league)
    input("Done")