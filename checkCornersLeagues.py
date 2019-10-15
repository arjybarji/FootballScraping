
with open('Statsv2.csv',encoding="utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content]
leagues = dict()
for c in content:
    statsSplit = c.split(",")
    league = statsSplit[-2]
    corners = statsSplit[-3]
    if(len(corners) == 0):
        #print(statsSplit[0])
        if(league in leagues):
            leagues.update({league : leagues[league]+1})
        else:
            leagues.update({league : 1})

for c in leagues:
    if(leagues[c]>5):
        print(c)
input()