import sqlite3

database = 'allStats.db'
conn = sqlite3.connect(database)

def check(homeTeam,awayTeam,field):
    cursor = conn.cursor()
    
    cursor.execute("SELECT "+field+",gameWeek FROM stats WHERE homeTeam = ? OR awayTeam = ? ORDER BY date(gameWeek) ASC", (homeTeam,homeTeam,))
    homeTeamLast5=cursor.fetchall()
    print(homeTeam + " " + field + " Last 5 Games")
    print(homeTeamLast5[-5:])
    
    cursor.execute("SELECT "+field+",gameWeek FROM stats WHERE homeTeam = ? ORDER BY date(gameWeek) ASC", (homeTeam,))
    homeTeamLast5Home=cursor.fetchall()
    print(homeTeam + " " + field + " Last 5 Home Games")
    print(homeTeamLast5Home[-5:])
    
    cursor.execute("SELECT "+field+",gameWeek FROM stats WHERE homeTeam = ? OR awayTeam = ? ORDER BY date(gameWeek) ASC", (awayTeam,awayTeam,))
    awayTeamLast5=cursor.fetchall()
    print(awayTeam + " " + field + " Last 5 Games")
    print(awayTeamLast5[-5:])
    
    cursor.execute("SELECT "+field+",gameWeek FROM stats WHERE awayTeam = ? ORDER BY date(gameWeek) ASC", (awayTeam,))
    awayTeamLast5Away=cursor.fetchall()
    print(awayTeam + " " + field + " Last 5 Away Games")
    print(awayTeamLast5Away[-5:])
    


cursor = conn.cursor()
cursor.execute("SELECT DISTINCT(league) FROM stats")
leagues = dict()
count = 0
for l in cursor.fetchall():
    leagues.update({count:l[0]})
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

choices = ["firstHalfTotalGoals","btts","secondHalfTotalGoals","firstHalfTotalGoals,secondHalfTotalGoals","matchCorners","matchCards","matchGoals"]
count = 0
for c in choices:
    print(str(count) +". " + choices[count])
    count+=1
field = choices[int(input("Pick Field"))]

check(homeTeam,awayTeam,field)


