import sqlite3
import datetime
import time
import cornersCardsTeams
import winsound
import pandas as pd

def insertIntoDatabase():
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    with open('Statsv2.csv',encoding="utf8") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
   
    count = len(content)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM stats", ())
    for c in content:
        statsSplit = c.split(",")
        cursor.execute("SELECT * FROM stats WHERE gameID = ?", (statsSplit[-1],))
        data=cursor.fetchall()
        if(len(data)==0):
            #print("Inserting " + statsSplit[0] + " vs " + statsSplit[1])
            if(count%500==0):
                print(count)
            count = count-1
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
    
    if((homeTeamHomeCards-awayTeamAwayCards)>=1.2 and (homeTotalTeamCards-awayTotalTeamCards)>=1.2):
        #print(homeTeam)
        bets.write(date + "," +homeTeam +",0.0 Asian Card Handicap," +  league + "," + "N/A" + "\n")
    if((awayTeamAwayCards-homeTeamHomeCards)>=1.2 and (awayTotalTeamCards-homeTotalTeamCards)>=1.2):
        #print(awayTeam)
        bets.write(date + "," +awayTeam +",0.0 Asian Card Handicap," +  league + "," + "N/A" + "\n")
  
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
    
    if((homeTeamHomeCorners-awayTeamAwayCorners)>=4 and (homeTotalTeamCorners-awayTotalTeamCorners)>=4):
        #print(homeTeam)
        bets.write(date + "," +homeTeam + ",Corner Match Bet," +  league +  "," + "N/A" +"\n")
    if((awayTeamAwayCorners-homeTeamHomeCorners)>=4 and (awayTotalTeamCorners-homeTotalTeamCorners)>=4):
        #print(awayTeam)
        bets.write(date + "," +awayTeam + ",Corner Match Bet," +  league + "," + "N/A" + "\n")
        
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
        #print(homeTeam)
        bets.write(date + "," +homeTeam + ",Over "+str(int(float(num)-0.5))+" Team Cards," +  league + "," + "N/A" + "\n")
    if(homeTeamPercentHome < .1 and homeTeamPercentTotal < .1):
        #print(homeTeam)
        bets.write(date + "," +homeTeam + ",Under "+str(int(float(num)+0.5))+" Team Cards," +  league + "," + "N/A" + "\n")
    
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
        #print(awayTeam)
        bets.write(date + "," + awayTeam + ",Over "+str(int(float(num)-0.5))+" Team Cards," + league + "," + "N/A" +"\n")
    if(awayTeamPercentHome < .1 and awayTeamPercentTotal < .1):
        #print(awayTeam)
        bets.write(date + "," + awayTeam + ",Under "+str(int(float(num)+0.5))+" Team Cards," + league + "," + "N/A" + "\n")

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
        #print(homeTeam)
        bets.write(date + "," +homeTeam + ",Over "+str(int(float(num)-0.5))+" Team Corners," + league + "," + "N/A"+ "\n")
    if(homeTeamPercentHome < .1 and homeTeamPercentTotal < .1):
        #print(homeTeam)
        bets.write(date + "," +homeTeam + ",Under "+str(int(float(num)-0.5))+" Team Corners," + league + "," + "N/A"+"\n")
    
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
        #print(awayTeam)
        bets.write(date + "," +awayTeam + ",Over "+str(int(float(num)-0.5))+" Team Corners," +league + "," + "N/A"+"\n")
    if(awayTeamPercentHome < .15 and awayTeamPercentTotal < .15):
        #print(awayTeam)
        bets.write(date + "," +awayTeam + ",Under "+str(int(float(num)-0.5))+" Team Corners," + league + "," + "N/A"+"\n")   

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
        if(field == "matchGoals"):
            field = "Goals"         
        if(field == "firstHalfTotalGoals"):
            field = "FH Goal Line"
            bet = "1.0/1.5" 
        bets.write(date + "," +homeTeam + " vs " + awayTeam + "," + "Under " +bet + " " + field+"," + league + "," + "Averages" + "\n")
        #print("Under "+bet)
    if(homeGoals >upper )and (awayGoals >upper) and (homeTotalGoals >upper) and (awayTotalGoals >upper):
        if(field != "matchGoals" and field !="SH Goals"and field !="firstHalfTotalGoals"):
            bet = str(int(float(bet)-0.5))
        if(field == "matchGoals"):
            field = "Goals"
        if(field == "firstHalfTotalGoals"):
            field = "FH Goal Line"
            bet = "0.5/1.0"
        bets.write(date + "," +homeTeam + " vs " + awayTeam + "," + "Over " +bet+ " " + field+ "," +league +"," + "Averages" + "\n")
        #print("Over "+bet)
        
    
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
        function = "Percent"
    if(field == "secondHalfTotalGoals"):
        field = "SH Goals"
        function = "Percent"
    if(field == "matchCards"):
        field = "Match Cards"
        function = "N/A"
    if(field == "matchCorners"):
        field = "Corners"
        function = "N/A"
    if(bet == "1"):
        bet = "1.0"

    if(homeTeamHomeOver <lower) and (awayTeamAwayOver <lower) and (homeTeamTotalOver <lower) and (awayTeamTotalOver <lower):
        if(field != "matchGoals" and field !="SH Goals"):
            bet = str(int(float(bet)+0.5))
        if(field == "FH Goal Line"):
            bet = "1.0/1.5"
        if(field == "matchGoals"):
            field = "Goals" 
            function = "Percent"
        bets.write(date + "," +homeTeam + " vs " + awayTeam + ","  + "Under " +bet + " " + field + "," + league + "," + function + "\n")
        #print("Under "+bet)
    if(homeTeamHomeOver >upper )and (awayTeamAwayOver >upper) and (homeTeamTotalOver >upper) and (awayTeamTotalOver >upper):
        if(field != "matchGoals" and field !="SH Goals"):
            bet = str(int(float(bet)-0.5))
            if(int(bet) == 0):
                bet = "1.0"
        if(field == "matchGoals"):
            field = "Goals"
            function = "Percent"
        if(field == "FH Goal Line"):
            bet = "0.5/1.0"
        bets.write(date + "," +homeTeam + " vs " + awayTeam + "," + "Over " +bet+ " " + field+ "," +league +"," + function +"\n")
        #print("Over "+bet)

def goalInEachHalf(homeTeam,awayTeam,date,league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    upper = 0.8
    
    cursor.execute("SELECT COUNT(gameID) FROM stats WHERE homeTeam = ? AND firstHalfTotalGoals > 0.5 AND secondHalfTotalGoals > 0.5" , (homeTeam,))
    teamHomeOver=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(gameID) FROM stats WHERE homeTeam = ?" , (homeTeam,))
    teamHomeCount=cursor.fetchall()[0][0]
    homeTeamHomeOver = teamHomeOver/teamHomeCount
    cursor.execute("SELECT COUNT(gameID) FROM stats WHERE awayTeam = ? AND firstHalfTotalGoals > 0.5 AND secondHalfTotalGoals > 0.5", (homeTeam,))
    teamAwayOver=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(gameID) FROM stats WHERE awayTeam = ?" , (homeTeam,))
    teamAwayCount=cursor.fetchall()[0][0]
    homeTeamTotalOver = (teamHomeOver + teamAwayOver)/(teamHomeCount+teamAwayCount)

    cursor.execute("SELECT COUNT(gameID) FROM stats WHERE awayTeam = ? AND firstHalfTotalGoals > 0.5 AND secondHalfTotalGoals > 0.5" , (awayTeam,))
    teamAwayOver=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(gameID) FROM stats WHERE awayTeam = ?" , (awayTeam,))
    teamAwayCount=cursor.fetchall()[0][0]
    awayTeamAwayOver = teamAwayOver/teamAwayCount
    cursor.execute("SELECT COUNT(gameID) FROM stats WHERE homeTeam = ? AND firstHalfTotalGoals > 0.5 AND secondHalfTotalGoals > 0.5" , (awayTeam,))
    teamHomeOver=cursor.fetchall()[0][0]
    cursor.execute("SELECT COUNT(gameID) FROM stats WHERE homeTeam = ?" , (awayTeam,))
    teamHomeCount=cursor.fetchall()[0][0]
    awayTeamTotalOver = (teamHomeOver + teamAwayOver)/(teamHomeCount+teamAwayCount) 

    if(homeTeamHomeOver >upper )and (awayTeamAwayOver >upper) and (homeTeamTotalOver >upper) and (awayTeamTotalOver >upper):
        bets.write(date + "," +homeTeam + " vs " + awayTeam + "," + "Goal In Each Half" + "," +league + "\n")
        #print("Goal In Each Half")        

def BTTSStatsTotal(homeTeam,awayTeam,field,lower,upper,date,league):
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
        #print("BTTS No")
        bets.write(date + "," +homeTeam + " vs " + awayTeam + ","+field.upper()+" No"+ "," + league +"\n")
    if(homeBTTSHomePercent >upper) and (homeBTTSTotal >upper) and (awayBTTSAwayPercent >upper) and (awayBTTSTotal >upper):
        #print("BTTS Yes")
        bets.write(date + "," +homeTeam + " vs " + awayTeam+","+field.upper()+" Yes" + ","+ league +"\n")

def getArrays(homeTeam,awayTeam,date,league): 
    cursor = conn.cursor()
    
    cursor.execute("SELECT gameID FROM stats WHERE homeTeam = ? OR awayTeam = ? ORDER BY date(gameWeek) ASC", (homeTeam,homeTeam,))
    last5HomeGames=cursor.fetchall()[-5:]
    
    cursor.execute("SELECT gameID FROM stats WHERE homeTeam = ? ORDER BY date(gameWeek) ASC", (homeTeam,))
    last5HomeHome=cursor.fetchall()[-5:]
    
    cursor.execute("SELECT gameID FROM stats WHERE homeTeam = ? OR awayTeam = ? ORDER BY date(gameWeek) ASC", (awayTeam,awayTeam,))
    last5AwayGames=cursor.fetchall()[-5:]
    
    cursor.execute("SELECT gameID FROM stats WHERE awayTeam = ? ORDER BY date(gameWeek) ASC", (awayTeam,))
    last5AwayAway=cursor.fetchall()[-5:] 
    
    if(BTTSStats(last5HomeGames) == "Yes" and BTTSStats(last5AwayGames) == "Yes") and (BTTSStats(last5HomeHome) == "Yes" and BTTSStats(last5AwayAway) == "Yes"):
        #print(homeTeam + " vs " + awayTeam + " BTTS Yes")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "BTTS Yes" + "," + league + "\n")
    if(BTTSStats(last5HomeGames) == "No" and BTTSStats(last5AwayGames) == "No") and (BTTSStats(last5HomeHome) == "No" and BTTSStats(last5AwayAway) == "No"):
        #print(homeTeam + " vs " + awayTeam + " BTTS No")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "BTTS No" + "," + league + "\n")        

    if(GoalsStats(last5HomeGames) == "Over" and GoalsStats(last5AwayGames) == "Over") and (GoalsStats(last5HomeHome) == "Over" and GoalsStats(last5AwayAway) == "Over"):
        #print(homeTeam + " vs " + awayTeam + " Over 2.5")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 2.5 Goals" + "," + league + "\n")
    if(GoalsStats(last5HomeGames) == "Under" and GoalsStats(last5AwayGames) == "Under") and (GoalsStats(last5HomeHome) == "Under" and GoalsStats(last5AwayAway) == "Under"):
        #print(homeTeam + " vs " + awayTeam + " Under 2.5")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under 2.5 Goals" + "," + league + "\n")

    if(league != "National League CHANGE"):
        teams = homeTeam + "," + awayTeam
        if(FHGoalsStats(last5HomeGames,teams) == "Over" and FHGoalsStats(last5AwayGames,teams) == "Over") and (FHGoalsStats(last5HomeHome,teams) == "Over" and FHGoalsStats(last5AwayAway,teams) == "Over"):
            if(teams in over05Teams):            
                #print(homeTeam + " vs " + awayTeam + " Over 0.5/1.0")
                formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 0.5/1.0 FH Goal Line" + "," + league + "\n")
            else:
                #print(homeTeam + " vs " + awayTeam + " Over 1.0")
                formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 1.0 FH Goal Line" + "," + league + "\n")            
        if(FHGoalsStats(last5HomeGames,teams) == "Under" and FHGoalsStats(last5AwayGames,teams) == "Under") and (FHGoalsStats(last5HomeHome,teams) == "Under" and FHGoalsStats(last5AwayAway,teams) == "Under"):
            #print(homeTeam + " vs " + awayTeam + " Under 1.0")
            formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under 1.0/1.5 FH Goal Line" + "," + league + "\n")        
            
        if(SHGoalsStats(last5HomeGames) == "Over" and SHGoalsStats(last5AwayGames) == "Over") and (SHGoalsStats(last5HomeHome) == "Over" and SHGoalsStats(last5AwayAway) == "Over"):
            #print(homeTeam + " vs " + awayTeam + " Over 1.5")
            formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 1.5 SH Goals" + "," + league + "\n")
        if(SHGoalsStats(last5HomeGames) == "Under" and SHGoalsStats(last5AwayGames) == "Under") and (SHGoalsStats(last5HomeHome) == "Under" and SHGoalsStats(last5AwayAway) == "Under"):
            #print(homeTeam + " vs " + awayTeam + " Under 1.5")
            formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under 1.5 SH Goals" + "," + league + "\n")

        if(FHSHGoalStats(last5HomeGames) == "Over" and FHSHGoalStats(last5AwayGames) == "Over") and (FHSHGoalStats(last5HomeHome) == "Over" and FHSHGoalStats(last5AwayAway) == "Over"):
            #print(homeTeam + " vs " + awayTeam + " Goal Each Half")
            formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Goal In Each Half" + "," + league + "\n")
        if(FHSHGoalStats(last5HomeGames) == "Under" and FHSHGoalStats(last5AwayGames) == "Under") and (FHSHGoalStats(last5HomeHome) == "Under" and FHSHGoalStats(last5AwayAway) == "Under"):
            #print(homeTeam + " vs " + awayTeam + " Goal Each Half")
            formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Goal In Each Half" + "," + league + "\n")
        
    if(homeTeam in cardsTeams and awayTeam in cardsTeams):
        cardBetsForm(homeTeam,awayTeam,3.5,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway)
        cardBetsForm(homeTeam,awayTeam,4.5,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway)

    if(homeTeam in cornersTeams and awayTeam in cornersTeams):
        cornerBetsForm(homeTeam,awayTeam,10.5,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway)
        cornerBetsForm(homeTeam,awayTeam,9.5,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway)

def cornerBetsForm(homeTeam,awayTeam,num,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway):
    if(CornerStats(last5HomeGames,num) == "Over" and CornerStats(last5AwayGames,num) == "Over") and (CornerStats(last5HomeHome,num) == "Over" and CornerStats(last5AwayAway,num) == "Over"):
        #print(homeTeam + " vs " + awayTeam + " Over " + str(num-0.5))
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over " + str(int(num-0.5)) + " Match Corners" + "," + league + "\n")
    if(CornerStats(last5HomeGames,num) == "Under" and CornerStats(last5AwayGames,num) == "Under") and (CornerStats(last5HomeHome,num) == "Under" and CornerStats(last5AwayAway,num) == "Under"):
        #print(homeTeam + " vs " + awayTeam + " Under " + str(num-0.5))
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under " + str(int(num+0.5)) + " Match Corners" + "," + league + "\n")

def cardBetsForm(homeTeam,awayTeam,num,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway):
    if(CardsStats(last5HomeGames,num) == "Over" and CardsStats(last5AwayGames,num) == "Over") and (CardsStats(last5HomeHome,num) == "Over" and CardsStats(last5AwayAway,num) == "Over"):
        #print(homeTeam + " vs " + awayTeam + " Over " + str(num-0.5))
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over " + str(int(num-0.5)) + " Match Cards" + "," + league + "\n")
    if(CardsStats(last5HomeGames,num) == "Under" and CardsStats(last5AwayGames,num) == "Under") and (CardsStats(last5HomeHome,num) == "Under" and CardsStats(last5AwayAway,num) == "Under"):
        #print(homeTeam + " vs " + awayTeam + " Under " + str(num-0.5))
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under " + str(int(num+0.5)) + " Match Cards" + "," + league + "\n")        
    
more = 0.8
less = 0.2  
def BTTSStats(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT btts FROM stats WHERE gameID = ?", (str(id[0]),))
            if cursor.fetchall()[0][0] == "y":
                count+=1
        if((count/len(games))>=more):
            return "Yes"
        if((count/len(games))<=less):
            return "No"
    else:
        return False

def GoalsStats(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT matchGoals FROM stats WHERE gameID = ?", (str(id[0]),))
            if cursor.fetchall()[0][0] >2.5:
                count+=1
        if((count/len(games))>=more):
            return "Over"
        if((count/len(games))<=less):
            return "Under"
    else:
        return False
        
def FHSHGoalStats(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor2 = conn.cursor()
            cursor.execute("SELECT firstHalfTotalGoals FROM stats WHERE gameID = ?", (str(id[0]),))
            cursor2.execute("SELECT secondHalfTotalGoals FROM stats WHERE gameID = ?", (str(id[0]),))
            if cursor.fetchall()[0][0] >0.5 and cursor2.fetchall()[0][0] >0.5:
                count+=1
        if((count/len(games))>=more):
            return "Over"
        
        else:
            return False
    else:
        return False        

over05Teams = []

def FHGoalsStats(games,teams):
    if(len(games)==5):
        countpoint5 = 0
        countonepoint5 = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT firstHalfTotalGoals FROM stats WHERE gameID = ?", (str(id[0]),))
            val = cursor.fetchall()[0][0]
            if val >0.5:
                countpoint5+=1
            if val >1.5:
                countonepoint5+=1              
        if((countpoint5/len(games))>=1) and ((countonepoint5/len(games))<=0.4):
            over05Teams.append(teams)
            return "Over"
        if((countpoint5/len(games))>=1):
            return "Over"
        if((countonepoint5/len(games))<=0):
            return "Under"
    else:
        return False
        
def SHGoalsStats(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT secondHalfTotalGoals FROM stats WHERE gameID = ?", (str(id[0]),))
            if cursor.fetchall()[0][0] >1.5:
                count+=1
        if((count/len(games))>=1):
            return "Over"
        if((count/len(games))<=0):
            return "Under"
    else:
        return False
        
def CornerStats(games,number):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT matchCorners FROM stats WHERE gameID = ?", (str(id[0]),))
            fetch = cursor.fetchall()[0][0]
            if fetch == -1:
                return False
            if fetch > number:
                count+=1
        if((count/len(games))>=more):
            return "Over"
        if((count/len(games))<=less):
            return "Under"
    else:
        return False

def CardsStats(games,number):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT matchCards FROM stats WHERE gameID = ?", (str(id[0]),))
            fetch = cursor.fetchall()[0][0]
            if fetch == -1:
                return False
            if fetch > number:
                count+=1
        if((count/len(games))>=1):
            return "Over"
        if((count/len(games))<=0):
            return "Under"
    else:
        return False

def OneFiveGoalsStats(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT matchGoals FROM stats WHERE gameID = ?", (str(id[0]),))
            if cursor.fetchall()[0][0] >1.5:
                count+=1
        if((count/len(games))>=1):
            return "Over"
    else:
        return False
        
def predict(homeTeam,awayTeam,gameweek,date,league):

    #print(homeTeam + "," + awayTeam + "," + date)
    checkAvgGoals(homeTeam,awayTeam,"matchGoals",1.8,3.2,"2.5",date,league)
    teamPercentStats(homeTeam,awayTeam,"matchGoals",0.25,0.75,"2.5",date,league)

    BTTSStatsTotal(homeTeam,awayTeam,"btts",0.25,0.75,date,league)
    
    goalInEachHalf(homeTeam,awayTeam,date,league)
    
    if(league != "National League CHANGE"):
        checkAvgGoals(homeTeam,awayTeam,"firstHalfTotalGoals",0.45,1.55,"1.0",date,league)
        checkAvgGoals(homeTeam,awayTeam,"secondHalfTotalGoals",0.8,2.2,"1.5",date,league)
        teamPercentStats(homeTeam,awayTeam,"firstHalfTotalGoals",0.1,0.9,"0.5",date,league)
        teamPercentStats(homeTeam,awayTeam,"firstHalfTotalGoals",0.1,0.9,"1.5",date,league)
        teamPercentStats(homeTeam,awayTeam,"secondHalfTotalGoals",0.2,0.8,"1.5",date,league)
    
    if((homeTeam in cardsTeams) and (awayTeam in cardsTeams)):
        #Asian Card Handicap Averages
            #If team1 has 1 cards less than 2 avg H/A and Total
        asianCardHandicap(homeTeam,awayTeam,date,league)
        
        #Over/Under 4.5 Cards Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCards",0.1,0.9,"3.5",date,league)
        #Over/Under 5.5 Cards Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCards",0.1,0.9,"4.5",date,league)        
        #Over/Under 1.5 Team Cards H/A and Total
        #teamCards(homeTeam,awayTeam,date,league,"1.5")
        
        #Over/Under 4.5 Corners Percent 80/20 H/A and Total
        #teamCorners(homeTeam,awayTeam,date,league,"3.5")
        
        #Corner Match Bet
            #If Team1 has 2 Less than Team2 Taken vs Conc H/A and Total
            #So City have 5.5 Avg Taken Home and 5.6 Taken Total where West Ham have 3.4 Taken Home and 3.5 Taken Total. City have Corner Match Bet
        #cornerMatchBet(homeTeam,awayTeam,date,league)
    
    if((homeTeam in cornersTeams) and (awayTeam in cornersTeams)):    
        #Over/Under 10 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.1,0.9,"9.5",date,league)
        #Over/Under 10 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.1,0.9,"10.5",date,league)
        #Over/Under 10 Corners Percent 80/20 H/A and Total
        teamPercentStats(homeTeam,awayTeam,"matchCorners",0.1,0.9,"11.5",date,league)

      
leaguesDict = dict()

if __name__ == '__main__':
    start_time = time.time()
    cornersCardsTeams.cornersCardsTeamsx()
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
    
    with open('top5Teams.txt',encoding="utf8") as f:
        top5Teams = f.readlines()
    top5Teams = [x.strip() for x in top5Teams]
    
    for l in leaguesT:
        leaguesDict.update({l.split(",")[0] : l.split(",")[1]})

    bets = open("bets.csv","w",encoding="utf8")
    formBets = open("formBets.csv","w",encoding="utf8")
    oneFive = open("15.csv","w",encoding="utf8")

    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=30)
    tomorrow = tomorrow.strftime("%B")
    today = today.strftime("%B")
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    fixtureLeagues = []
    contentLength = len(content)
    for c in content:
        if(contentLength%50==0):
            print(contentLength)
        contentLength-=1
        split = c.split(",")
        homeTeam = split[0]
        awayTeam = split[1]
        gameweek = split[2]
        leagueFixtures = split[4]
        if(leagueFixtures not in fixtureLeagues):
            fixtureLeagues.append(leagueFixtures)
        cursor.execute("SELECT COUNT(gameID) FROM stats WHERE homeTeam = ? OR awayTeam = ?", (homeTeam,homeTeam,))
        dataH=cursor.fetchall()[0][0]
        cursor.execute("SELECT COUNT(gameID) FROM stats WHERE homeTeam = ? OR awayTeam = ?", (awayTeam,awayTeam,))
        dataA=cursor.fetchall()[0][0]
        use = dataH>7 and dataA>7
        date = split[3]
        league = leaguesDict[split[4]]
        #if(today.lower() in date.lower() and use) or (tomorrow.lower() in date.lower() and use):
        if(date.split("/")[1] == "06" and use):
        #if(use):
            predict(homeTeam,awayTeam,gameweek,date,league)
            getArrays(homeTeam,awayTeam,date,league)
    bets.close()
    temp = []
    print(fixtureLeagues)
    with open('bets.csv',encoding="utf8") as f:
        bets2 = f.readlines()
    bets2 = [x.strip() for x in bets2]
    f.close()
    bets3 = open("bets.csv","w",encoding="utf8")
    for b in bets2:
        if(b not in temp):
            bets3.write(b + "\n")
            temp.append(b)
    
    with open('bets.csv',encoding="utf8") as f:
        bets2 = f.readlines()
    bets2 = [x.strip() for x in bets2]
    formBets.close()
    bets3.close()
    oneFive.close()
    try:
        formBetsPD = pd.read_csv('formBets.csv',header = None)
        betsPD = pd.read_csv('bets.csv',header = None,usecols=[0,1,2,3])
        merged = pd.merge(betsPD, formBetsPD, how='inner')
        merged.to_csv('combinedBets.csv',index=False,header=False)
    except:
        pass
    
    with open('Statsv2.csv',encoding="utf8") as f:
        statsFile = f.readlines()
    statsFile = [x.strip() for x in statsFile]
    newStats = open("StatsForCompare.csv","w",encoding="utf8")
    for s in statsFile:
        if(s.split(",")[-2] in fixtureLeagues):
            newStats.write(s+"\n")
    
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)     
    
    print("--- %s minutes ---" % ((time.time() - start_time)/60))
    input("Done")
