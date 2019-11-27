import datetime
now = datetime.datetime.now()

with open("Statsv2.csv","r",encoding = "utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content]

right = "Premier League - Ukraine"
stats = open("newStats.csv","w",encoding = "utf8")
leagueFile = open(right + " ending in "+str(now.year)+ " .csv","w",encoding = "utf8")



for c in content:
    league = c.split(",")[-2]
    if(league == right):
        leagueFile.write(c + "\n")
    else:
        stats.write(c + "\n")