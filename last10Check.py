import sqlite3

def check(homeTeam,awayTeam,field):
    database = 'allStats.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute("SELECT "+field+" FROM stats WHERE homeTeam = ? OR awayTeam = ?", (homeTeam,homeTeam,))
    homeTeamLast5=cursor.fetchall()
    print(homeTeam + " " + field + " Last 5 Games")
    print(homeTeamLast5[-5:])
    
    cursor.execute("SELECT "+field+" FROM stats WHERE homeTeam = ?", (homeTeam,))
    homeTeamLast5Home=cursor.fetchall()
    print(homeTeam + " " + field + " Last 5 Home Games")
    print(homeTeamLast5Home[-5:])
    
    cursor.execute("SELECT "+field+" FROM stats WHERE homeTeam = ? OR awayTeam = ?", (awayTeam,awayTeam,))
    awayTeamLast5=cursor.fetchall()
    print(awayTeam + " " + field + " Last 5 Games")
    print(awayTeamLast5[-5:])
    
    cursor.execute("SELECT "+field+" FROM stats WHERE awayTeam = ?", (awayTeam,))
    awayTeamLast5Away=cursor.fetchall()
    print(awayTeam + " " + field + " Last 5 Away Games")
    print(awayTeamLast5Away[-5:])
    
    
homeTeam = "Rio Ave"
awayTeam = "Gil Vicente"
field = "firstHalfTotalGoals"
#field = "btts"
#field = "secondHalfTotalGoals"
#field = "firstHalfTotalGoals,secondHalfTotalGoals"
#field = "matchCorners"
check(homeTeam,awayTeam,field)
input()
