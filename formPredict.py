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
    
    if(e2or3Goals(last5HomeGames) == "Yes" and e2or3Goals(last5AwayGames) == "Yes") and (e2or3Goals(last5HomeHome) == "Yes" and e2or3Goals(last5AwayAway) == "Yes"):
        print(homeTeam + " vs " + awayTeam + " 2 or 3 Match Goals")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "2 or 3 Match Goals" + "," + league + "\n")
    
    '''
    if(BTTSStats(last5HomeGames) == "Yes" and BTTSStats(last5AwayGames) == "Yes") and (BTTSStats(last5HomeHome) == "Yes" and BTTSStats(last5AwayAway) == "Yes"):
        print(homeTeam + " vs " + awayTeam + " BTTS Yes")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "BTTS Yes" + "," + league + "\n")
    if(BTTSStats(last5HomeGames) == "No" and BTTSStats(last5AwayGames) == "No") and (BTTSStats(last5HomeHome) == "No" and BTTSStats(last5AwayAway) == "No"):
        print(homeTeam + " vs " + awayTeam + " BTTS No")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "BTTS No" + "," + league + "\n")        

    if(GoalsStats(last5HomeGames) == "Over" and GoalsStats(last5AwayGames) == "Over") and (GoalsStats(last5HomeHome) == "Over" and GoalsStats(last5AwayAway) == "Over"):
        print(homeTeam + " vs " + awayTeam + " Over 2.5")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 2.5 Goals" + "," + league + "\n")
    if(GoalsStats(last5HomeGames) == "Under" and GoalsStats(last5AwayGames) == "Under") and (GoalsStats(last5HomeHome) == "Under" and GoalsStats(last5AwayAway) == "Under"):
        print(homeTeam + " vs " + awayTeam + " Under 2.5")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under 2.5 Goals" + "," + league + "\n")

    teams = homeTeam + "," + awayTeam
    if(FHGoalsStats(last5HomeGames,teams) == "Over" and FHGoalsStats(last5AwayGames,teams) == "Over") and (FHGoalsStats(last5HomeHome,teams) == "Over" and FHGoalsStats(last5AwayAway,teams) == "Over"):
        if(teams in over05Teams):            
            print(homeTeam + " vs " + awayTeam + " Over 0.5/1.0")
            formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 0.5/1.0 FH Goal Line" + "," + league + "\n")
        else:
            print(homeTeam + " vs " + awayTeam + " Over 1.0")
            formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 1.0 FH Goal Line" + "," + league + "\n")            
    if(FHGoalsStats(last5HomeGames,teams) == "Under" and FHGoalsStats(last5AwayGames,teams) == "Under") and (FHGoalsStats(last5HomeHome,teams) == "Under" and FHGoalsStats(last5AwayAway,teams) == "Under"):
        print(homeTeam + " vs " + awayTeam + " Under 1.0")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under 1.0 FH Goal Line" + "," + league + "\n")        
        
    if(SHGoalsStats(last5HomeGames) == "Over" and SHGoalsStats(last5AwayGames) == "Over") and (SHGoalsStats(last5HomeHome) == "Over" and SHGoalsStats(last5AwayAway) == "Over"):
        print(homeTeam + " vs " + awayTeam + " Over 1.5")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over 1.5 SH Goals" + "," + league + "\n")
    if(SHGoalsStats(last5HomeGames) == "Under" and SHGoalsStats(last5AwayGames) == "Under") and (SHGoalsStats(last5HomeHome) == "Under" and SHGoalsStats(last5AwayAway) == "Under"):
        print(homeTeam + " vs " + awayTeam + " Under 1.5")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under 1.5 SH Goals" + "," + league + "\n")

    if(FHSHGoalStats(last5HomeGames) == "Over" and FHSHGoalStats(last5AwayGames) == "Over") and (FHSHGoalStats(last5HomeHome) == "Over" and FHSHGoalStats(last5AwayAway) == "Over"):
        print(homeTeam + " vs " + awayTeam + " Goal Each Half")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Goal In Each Half" + "," + league + "\n")
    if(FHSHGoalStats(last5HomeGames) == "Under" and FHSHGoalStats(last5AwayGames) == "Under") and (FHSHGoalStats(last5HomeHome) == "Under" and FHSHGoalStats(last5AwayAway) == "Under"):
        print(homeTeam + " vs " + awayTeam + " Goal Each Half")
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Goal In Each Half" + "," + league + "\n")
    
    cornerBetsForm(homeTeam,awayTeam,10.5,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway)
    cornerBetsForm(homeTeam,awayTeam,9.5,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway)
    
    cardBetsForm(homeTeam,awayTeam,3.5,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway)
    cardBetsForm(homeTeam,awayTeam,4.5,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway)
    '''

def cornerBetsForm(homeTeam,awayTeam,num,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway):
    if(CornerStats(last5HomeGames,num) == "Over" and CornerStats(last5AwayGames,num) == "Over") and (CornerStats(last5HomeHome,num) == "Over" and CornerStats(last5AwayAway,num) == "Over"):
        print(homeTeam + " vs " + awayTeam + " Over " + str(num-0.5))
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over " + str(int(num-0.5)) + " Match Corners" + "," + league + "\n")
    if(CornerStats(last5HomeGames,num) == "Under" and CornerStats(last5AwayGames,num) == "Under") and (CornerStats(last5HomeHome,num) == "Under" and CornerStats(last5AwayAway,num) == "Under"):
        print(homeTeam + " vs " + awayTeam + " Under " + str(num-0.5))
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under " + str(int(num+0.5)) + " Match Corners" + "," + league + "\n")

def cardBetsForm(homeTeam,awayTeam,num,date,league,last5HomeGames,last5HomeHome,last5AwayGames,last5AwayAway):
    if(CardsStats(last5HomeGames,num) == "Over" and CardsStats(last5AwayGames,num) == "Over") and (CardsStats(last5HomeHome,num) == "Over" and CardsStats(last5AwayAway,num) == "Over"):
        print(homeTeam + " vs " + awayTeam + " Over " + str(num-0.5))
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Over " + str(int(num-0.5)) + " Match Cards" + "," + league + "\n")
    if(CardsStats(last5HomeGames,num) == "Under" and CardsStats(last5AwayGames,num) == "Under") and (CardsStats(last5HomeHome,num) == "Under" and CardsStats(last5AwayAway,num) == "Under"):
        print(homeTeam + " vs " + awayTeam + " Under " + str(num-0.5))
        formBets.write(date + ","+ homeTeam + " vs " + awayTeam + "," + "Under " + str(int(num+0.5)) + " Match Cards" + "," + league + "\n")        
        
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
        
def e2or3Goals(games):
    if(len(games)==5):
        count = 0
        for id in games:
            cursor = conn.cursor()
            cursor.execute("SELECT matchGoals FROM stats WHERE gameID = ?", (str(id[0]),))
            fetch = cursor.fetchall()[0][0]
            if fetch == 2 or fetch == 3:
                count+=1
        if((count/len(games))>=0.6):
            return "Yes"
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
        if((count/len(games))>=0.8):
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
        if((countpoint5/len(games))>=.8) and ((countonepoint5/len(games))<=0.2):
            over05Teams.append(teams)
        if((countpoint5/len(games))>=.8):
            return "Over"
        if((countpoint5/len(games))<=0.2):
            return "Under"
        if((countonepoint5/len(games))>=.8):
            return "Over"
        if((countonepoint5/len(games))<=0.2):
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
        if((count/len(games))>=.8):
            return "Over"
        if((count/len(games))<=0.2):
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
        if((count/len(games))>=.8):
            return "Over"
        if((count/len(games))<=0.2):
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
        if((count/len(games))>=.8):
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

formBets = open("AllformBets.csv","w",encoding="utf8")

for l in leaguesT:
    leaguesDict.update({l.split(",")[0] : l.split(",")[1]})

today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=30)
tomorrow = tomorrow.strftime("%B")
todayYD = str(int(today.strftime("%d"))-1)
todayD = today.strftime("%d")
todayM = today.strftime("%B")


start_time = time.time()

for c in content:
    split = c.split(",")
    homeTeam = split[0]
    awayTeam = split[1]
    date = split[3]
    league = leaguesDict[split[4]]
    #if(todayD.lower() in date.lower() and todayM.lower() in date.lower() or todayYD.lower() in date.lower() and todayM.lower() in date.lower()):
    if(todayM.lower() in date.lower()):
        getArrays(homeTeam,awayTeam,date,league)

print("--- %s minutes ---" % ((time.time() - start_time)/60))
input("Done")
