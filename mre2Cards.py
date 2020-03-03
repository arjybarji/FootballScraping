import sqlite3
import datetime
import time
import cornersCardsTeams
import winsound

database = 'allStats.db'
conn = sqlite3.connect(database)

def getArrays(homeTeam,awayTeam,date,league): 
    cursor = conn.cursor()
    
    cursor.execute("SELECT gameID FROM stats WHERE homeTeam = ? OR awayTeam = ?", (homeTeam,homeTeam,))
    last5HomeGames=cursor.fetchall()[-5:]
    
    cursor.execute("SELECT gameID FROM stats WHERE homeTeam = ?", (homeTeam,))
    last5HomeHome=cursor.fetchall()[-5:]
    
    cursor.execute("SELECT gameID FROM stats WHERE homeTeam = ? OR awayTeam = ?", (awayTeam,awayTeam,))
    last5AwayGames=cursor.fetchall()[-5:]
    
    cursor.execute("SELECT gameID FROM stats WHERE awayTeam = ?", (awayTeam,))
    last5AwayAway=cursor.fetchall()[-5:]
    if(getCorners(last5HomeGames) and getCorners(last5HomeHome) and getCorners(last5AwayGames) and getCorners(last5AwayAway)):
        corners2.write(homeTeam + " vs " +  awayTeam + "," + league + "," + date + "\n")
    
def getCorners(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT homeCorners,awayCorners,gameWeek FROM stats WHERE gameID = ?", (str(id[0]),))
            fetch = cursor.fetchall()[0]
            if fetch[0] == -1 or fetch[1] == -1:
                return False
            if fetch[0] > 1 and fetch[1] > 1:
                count+=1
        if((count/len(games))>=1):
            return True
            
    else:
        return False

with open('fixturesv2.csv',encoding="utf8") as f:
        content = f.readlines()
content = [x.strip() for x in content]

with open('leagueTransform.csv',encoding="utf8") as f:
    leaguesT = f.readlines()
leaguesT = [x.strip() for x in leaguesT]

leaguesDict = dict()

corners2 = open("corners2.csv","w",encoding="utf8")

for l in leaguesT:
    leaguesDict.update({l.split(",")[0] : l.split(",")[1]})

today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=30)
tomorrow = tomorrow.strftime("%B")
todayYD = str(int(today.strftime("%d"))-1)
todayD = today.strftime("%d")
todayM = today.strftime("%B")

for c in content:
    split = c.split(",")
    homeTeam = split[0]
    awayTeam = split[1]
    date = split[3]
    league = leaguesDict[split[4]]
    #if(todayD.lower() in date.lower() and todayM.lower() in date.lower() or todayYD.lower() in date.lower() and todayM.lower() in date.lower()):
    if(todayM.lower() in date.lower()):
        getArrays(homeTeam,awayTeam,date,league)