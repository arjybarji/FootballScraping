
statsadd = []
with open("Statsv2.csv","r",encoding = "utf8") as f:
    Statsv2 = f.readlines()
Statsv2 = [x.strip() for x in Statsv2]
newstats = open("NewStats.csv","w",encoding="utf8")


for s in Statsv2:
    if(s not in statsadd):
        statsadd.append(s)
        newstats.write(s + "\n")
    else:
        print(s)
     