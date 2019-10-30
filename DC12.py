
with open('Statsv2.csv',encoding="utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content]

startingAmount = 100
DC12 = 1.2
stake = 1
draws = 0
notDraws = 0
for c in content:
    statsSplit = c.split(",")
    homeGoals = int(statsSplit[3])
    awayGoals = int(statsSplit[4])
    if(homeGoals == awayGoals):
        startingAmount = startingAmount-stake
        draws +=1
    else:
        startingAmount = startingAmount - stake
        startingAmount = startingAmount + (stake*DC12)
        notDraws +=1
        
print(startingAmount)
print("Draws: " + str(draws))
print("Not Draws: " + str(notDraws))

input()