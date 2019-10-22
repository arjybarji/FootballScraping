
with open('fixturesv2.csv',encoding="utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content]
dates = dict()
for c in content:
    statsSplit = c.split(",")
    date = statsSplit[3]
    if(int(statsSplit[2]) > 7):
        #print(statsSplit[0])
        if(date in dates):
            dates.update({date : dates[date]+1})
        else:
            dates.update({date : 1})

for c in dates:
    if("october" in c.lower()):
        print(c + ":" + str(dates[c]))
input()