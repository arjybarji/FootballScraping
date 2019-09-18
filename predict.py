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
            cursor.execute("INSERT INTO stats(homeTeam,awayTeam,gameWeek,homeGoals,awayGoals,matchGoals,BTTS,firstHalfHomeGoals,firstHalfHomeConc,firstHalfAwayGoals,firstHalfAwayConc,firstHalfTotalGoals,secondHalfHomeGoals,secondHalfHomeConc,secondHalfAwayGoals,secondHalfAwayConc,secondHalfTotalGoals,league,gameID) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(statsSplit[0],statsSplit[1],statsSplit[2],int(statsSplit[3]),int(statsSplit[4]),int(statsSplit[5]),statsSplit[6],int(statsSplit[7]),int(statsSplit[8]),int(statsSplit[9]),int(statsSplit[10]),int(statsSplit[11]),int(statsSplit[12]),int(statsSplit[13]),int(statsSplit[14]),int(statsSplit[15]),int(statsSplit[16]),statsSplit[25],int(statsSplit[26]),))
    conn.commit()
    cursor.close()
    conn.close()

def checkAvgGoals(homeTeam,awayTeam,field,lower,upper,bet):
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
    field = field + " averages"
    if(homeGoals <lower) and (awayGoals <lower) and (homeTotalGoals <lower) and (awayTotalGoals <lower):
        bets.write(field + "," + homeTeam + "," + str(homeGoals) + "," + awayTeam + "," + str(awayGoals) + "," + "Under " +bet + "\n")
        print("Under "+bet+" because of H/A")
    if(homeGoals >upper )and (awayGoals >upper) and (homeTotalGoals >upper) and (awayTotalGoals >upper):
        bets.write(field + "," + homeTeam + "," + str(homeGoals) + "," + awayTeam + "," + str(awayGoals) + "," + "Over " +bet+ "\n")
        print("Over "+bet+" because of H/A")
    
def teamPercentStats(homeTeam,awayTeam,field,lower,upper,bet):
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
    field = field + " percent"
    if(homeTeamHomeOver <lower) and (awayTeamAwayOver <lower) and (homeTeamTotalOver <lower) and (awayTeamTotalOver <lower):
        bets.write(field + "," + homeTeam + "," + str(homeTeamHomeOver) + "," + awayTeam + "," + str(awayTeamAwayOver) + "," + "Under " +bet + "\n")
        print("Under "+bet+" because of H/A")
    if(homeTeamHomeOver >upper )and (awayTeamAwayOver >upper) and (homeTeamTotalOver >upper) and (awayTeamTotalOver >upper):
        bets.write(field + "," + homeTeam + "," + str(homeTeamHomeOver) + "," + awayTeam + "," + str(awayTeamAwayOver) + "," + "Over " +bet+ "\n")
        print("Over "+bet+" because of H/A")
    

def predict(homeTeam,awayTeam,gameweek,date,league):
    print(homeTeam + " vs " + awayTeam)
    checkAvgGoals(homeTeam,awayTeam,"matchGoals",2,3,"2.5")
    checkAvgGoals(homeTeam,awayTeam,"firstHalfTotalGoals",0.65,1.35,"1.0")
    #checkAvgGoals(homeTeam,awayTeam,"secondHalfTotalGoals",0.7,1.3,"1.0") 
    teamPercentStats(homeTeam,awayTeam,"matchGoals",0.25,0.75,"2.5")
    #teamPercentStats(homeTeam,awayTeam,"matchGoals",0.25,0.75,"3.5")
    teamPercentStats(homeTeam,awayTeam,"firstHalfTotalGoals ",0.2,0.8,"1")
    #teamPercentStats(homeTeam,awayTeam,"firstHalfTotalGoals ",0.2,0.8,"1.5")

if __name__ == '__main__':
    insertIntoDatabase()
    with open('fixturesv2.csv',encoding="utf8") as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    bets = open("bets.csv","w",encoding="utf8")
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tomorrow = tomorrow.strftime("%d %B %Y")
    today = today.strftime("%d %B %Y")
    for c in content:
        split = c.split(",")
        homeTeam = split[0]
        awayTeam = split[1]
        gameweek = split[2]
        date = split[3]
        league = split[4]
        if(date == today and int(gameweek)>7):
        #if("september" in date.lower() and int(gameweek)>7):
            predict(homeTeam,awayTeam,gameweek,date,league)