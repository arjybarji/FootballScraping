import sqlite3

toWrite = dict()

def getAverages(league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    if(league not in toWrite):
        toWrite.update({league:""})
    for field in fields:
        cursor.execute("SELECT AVG("+field+") FROM stats WHERE league = ?", (league,))
        result=cursor.fetchall()[0][0]
        toWrite.update({league:toWrite[league]+str(result)+","})
    conn.close()

def getPercent(league):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    print(league)
    for field in fieldsPerc:
        over = field.split(",")[1]
        field = field.split(",")[0]
        cursor.execute("SELECT count("+field+") FROM stats WHERE league = ? AND " + field + " > " +over, (league,))
        count=cursor.fetchall()[0][0]
        cursor.execute("SELECT count("+field+") FROM stats WHERE league = ?", (league,))
        total=cursor.fetchall()[0][0]
        toWrite.update({league:toWrite[league]+str(count/total)+","})
    conn.close()

averages = open("leagueAverages.csv","w",encoding = "utf8")
averages.write("League,matchGoalsAvg,firstHalfTotalGoalsAvg,secondHalfTotalGoalsAvg,matchCardsAvg,matchGoals2.5,firstHalfTotalGoals0.5,secondHalfTotalGoals0.5,matchCards3.5,matchCards4.5"+"\n")
with open('fixturesv2.csv',encoding="utf8") as f:
        content = f.readlines()
content = [x.strip() for x in content]
leagues = []
for c in content:
    league = c.split(",")[4]
    if(league not in leagues):
        leagues.append(league)

fields = ["matchGoals","firstHalfTotalGoals","secondHalfTotalGoals","matchCards"]
fieldsPerc = ["matchGoals,2.5","firstHalfTotalGoals,0.5","secondHalfTotalGoals,0.5","matchCards,3.5","matchCards,4.5"]
for league in leagues:
    getAverages(league)
    getPercent(league)

for l in toWrite:
    averages.write(l+"," + toWrite[l]+"\n")

   