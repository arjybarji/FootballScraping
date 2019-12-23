from datetime import datetime
import sqlite3

with open("fixturesv2.csv","r",encoding = "utf8") as f:
    fixturesv2 = f.readlines()
fixturesv2 = [x.strip() for x in fixturesv2]

database = 'fixtures.db'
conn = sqlite3.connect(database)
cursor = conn.cursor()


for f in fixturesv2:
    homeTeam = f.split(",")[0]
    awayTeam = f.split(",")[1]
    gameWeek = f.split(",")[2]
    date = f.split(",")[3]
    league = f.split(",")[4]
    id = f.split(",")[5]
    datetime_object = datetime.strptime(date, '%d %B %Y')
    cursor.execute("INSERT INTO fixtures(homeTeam,awayTeam,gameWeek,date,league,id) VALUES (?,?,?,?,?,?)",(homeTeam,awayTeam,gameWeek,datetime_object,league,id))
    
    print(date + "    :     "+str(datetime_object))
#    print(type(datetime_object.date()))
    
conn.commit()
cursor.close()
conn.close()