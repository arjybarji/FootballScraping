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
    last5HomeGamesBTTS = BTTSStats(last5HomeGames)
    last5HomeGamesGoals = GoalsStats(last5HomeGames)
    last5HomeGamesFHGoals = FHGoalsStats(last5HomeGames)
    
    cursor.execute("SELECT gameID FROM stats WHERE homeTeam = ?", (homeTeam,))
    last5HomeHome=cursor.fetchall()[-5:]
    last5HomeHomeBTTS = BTTSStats(last5HomeHome)
    last5HomeHomeGoals = GoalsStats(last5HomeHome)
    last5HomeHomeFHGoals = FHGoalsStats(last5HomeHome)
    
    cursor.execute("SELECT gameID FROM stats WHERE homeTeam = ? OR awayTeam = ?", (awayTeam,awayTeam,))
    last5AwayGames=cursor.fetchall()[-5:]
    last5AwayGamesBTTS = BTTSStats(last5AwayGames)
    last5AwayGamesGoals = GoalsStats(last5AwayGames)
    last5AwayGamesFHGoals = FHGoalsStats(last5AwayGames)
    
    cursor.execute("SELECT gameID FROM stats WHERE awayTeam = ?", (awayTeam,))
    last5AwayAway=cursor.fetchall()[-5:]
    last5AwayAwayBTTS = BTTSStats(last5AwayAway)
    last5AwayAwayGoals = GoalsStats(last5AwayAway)
    last5AwayAwayFHGoals = FHGoalsStats(last5AwayAway)
    
    if(last5HomeGamesBTTS == "Yes" and last5AwayGamesBTTS == "Yes") and (last5HomeHomeBTTS == "Yes" and last5AwayAwayBTTS == "Yes"):
        print(homeTeam + " vs " + awayTeam + " BTTS Yes")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "BTTS Yes" + "," + league + "\n")
    if(last5HomeGamesBTTS == "No" and last5AwayGamesBTTS == "No") and (last5HomeHomeBTTS == "No" and last5AwayAwayBTTS == "No"):
        print(homeTeam + " vs " + awayTeam + " BTTS No")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "BTTS No" + "," + league + "\n")        
    if(last5HomeGamesGoals == "Over" and last5AwayGamesGoals == "Over") and (last5HomeHomeGoals == "Over" and last5AwayAwayGoals == "Over"):
        print(homeTeam + " vs " + awayTeam + " Over 2.5")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 2.5 Goals" + "," + league + "\n")
    if(last5HomeGamesGoals == "Under" and last5AwayGamesGoals == "Under") and (last5HomeHomeGoals == "Under" and last5AwayAwayGoals == "Under"):
        print(homeTeam + " vs " + awayTeam + " Under 2.5")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under 2.5 Goals" + "," + league + "\n")
    if(last5HomeGamesFHGoals == "Over" and last5AwayGamesFHGoals == "Over") and (last5HomeHomeFHGoals == "Over" and last5AwayAwayFHGoals == "Over"):
        print(homeTeam + " vs " + awayTeam + " Over 1.0")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 1.0 FH Goal Line" + "," + league + "\n")
    if(last5HomeGamesFHGoals == "Under" and last5AwayGamesFHGoals == "Under") and (last5HomeHomeFHGoals == "Under" and last5AwayAwayFHGoals == "Under"):
        print(homeTeam + " vs " + awayTeam + " Under 1.0")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under 1.0 FH Goal Line" + "," + league + "\n")
        
    
def BTTSStats(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT btts FROM stats WHERE gameID = ?", (str(id[0]),))
            if cursor.fetchall()[0][0] == "y":
                count+=1
        if((count/len(games))>=0.8):
            return "Yes"
        if((count/len(games))<=0.2):
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
        if((count/len(games))>=0.8):
            return "Over"
        if((count/len(games))<=0.2):
            return "Under"
    else:
        return False

def FHGoalsStats(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT firstHalfTotalGoals FROM stats WHERE gameID = ?", (str(id[0]),))
            if cursor.fetchall()[0][0] >0.5:
                count+=1
        if((count/len(games))>=0.8):
            return "Over"
        if((count/len(games))<=0.2):
            return "Under"
    else:
        return False

with open('fixturesv2.csv',encoding="utf8") as f:
        content = f.readlines()
content = [x.strip() for x in content]
    
with open('leagueTransform.csv',encoding="utf8") as f:
    leaguesT = f.readlines()
leaguesT = [x.strip() for x in leaguesT]

leaguesDict = dict()



for l in leaguesT:
    leaguesDict.update({l.split(",")[0] : l.split(",")[1]})

today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=30)
tomorrow = tomorrow.strftime("%B")
today = today.strftime("%B")

start_time = time.time()

for c in content:
    split = c.split(",")
    homeTeam = split[0]
    awayTeam = split[1]
    date = split[3]
    league = leaguesDict[split[4]]
    if(today.lower() in date.lower()):
    #if(today.lower() in date.lower()) or (tomorrow.lower() in date.lower()):
        getArrays(homeTeam,awayTeam,date,league)

print("--- %s minutes ---" % ((time.time() - start_time)/60))
input("Done")
