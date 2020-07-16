import sqlite3
import pandas as pd

database = 'allStats.db'
conn = sqlite3.connect(database)

def check(homeTeam,awayTeam,field,games):
    cursor = conn.cursor()
    
    cursor.execute("SELECT "+field+" FROM stats WHERE homeTeam = ? OR awayTeam = ? ORDER BY date(gameWeek) ASC", (homeTeam,homeTeam,))
    homeTeamLast5=cursor.fetchall()
    print(homeTeam + " " + field + " Last "+str(games)+" Games")
    print(homeTeamLast5[games:])
    
    cursor.execute("SELECT "+field+" FROM stats WHERE homeTeam = ? ORDER BY date(gameWeek) ASC", (homeTeam,))
    homeTeamLast5Home=cursor.fetchall()
    print(homeTeam + " " + field + " Last "+str(games)+" Home Games")
    print(homeTeamLast5Home[games:])
    
    cursor.execute("SELECT "+field+" FROM stats WHERE homeTeam = ? OR awayTeam = ? ORDER BY date(gameWeek) ASC", (awayTeam,awayTeam,))
    awayTeamLast5=cursor.fetchall()
    print(awayTeam + " " + field + " Last "+str(games)+" Games")
    print(awayTeamLast5[games:])
    
    cursor.execute("SELECT "+field+" FROM stats WHERE awayTeam = ? ORDER BY date(gameWeek) ASC", (awayTeam,))
    awayTeamLast5Away=cursor.fetchall()
    print(awayTeam + " " + field + " Last "+str(games)+" Away Games")
    print(awayTeamLast5Away[games:])
    


content = pd.read_csv("fixturesv2.csv",header = None)[4].unique()

gameChoice = -1*int(input("How many games back?"))

leagues = dict()
count = 0
for l in content:
    leagues.update({count:l})
    count +=1

for l in leagues:
    print(str(l) + ". " + leagues[l])


leagueChoice = leagues[int(input("Select League"))]
print(leagueChoice)

teams = dict()
count = 0
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT(homeTeam) FROM stats WHERE league = ? ORDER BY homeTeam ASC", (leagueChoice,))
for t in cursor.fetchall():
    teams.update({count:t[0]})
    count +=1

for t in teams:
    print(str(t) + ". " + teams[t])

teamChoice = input("Select Teams")
homeTeam = teams[int(teamChoice.split(",")[0])]
awayTeam = teams[int(teamChoice.split(",")[1])]

choices = ["firstHalfTotalGoals","btts","secondHalfTotalGoals","firstHalfTotalGoals,secondHalfTotalGoals","matchCorners","matchCards","matchGoals","homeTeamCards,awayTeamCards"]
count = 0
for c in choices:
    print(str(count) +". " + choices[count])
    count+=1
field = choices[int(input("Pick Field"))]

check(homeTeam,awayTeam,field,gameChoice)

