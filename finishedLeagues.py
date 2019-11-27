
with open("Statsv2.csv","r",encoding = "utf8") as f:
    Statsv2 = f.readlines()
Statsv2 = [x.strip() for x in Statsv2]

with open("fixturesv2.csv","r",encoding = "utf8") as f:
    fixturesv2 = f.readlines()
fixturesv2 = [x.strip() for x in fixturesv2]

fixtures = []

for f in fixturesv2:
    league = f.split(",")[-2]
    if(league not in fixtures):
        fixtures.append(league)
    
done = []

for s in Statsv2:
    league = s.split(",")[-2]
    gameweek = int(f.split(",")[2])
    if(league not in done and league not in fixtures):
        done.append(league)
print(done)
input("")