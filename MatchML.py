import sqlite3
import pandas as pd

database = 'allStats.db'
conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute("SELECT DISTINCT(league) from stats")
leagues = list(cursor.fetchall())


for league in leagues:
    cursor.execute("SELECT avg(matchGoals) from stats WHERE league = ?", (league[0],))

    print(league[0] + ": " + str(cursor.fetchall()[0][0]))

with sqlite3.connect('allStats.db') as con:
    matches = pd.read_sql_query("SELECT homeTeam,awayTeam,homeGoals,awayGoals,matchGoals from stats", con)

#print(matches.describe())
#print(matches.tail())    