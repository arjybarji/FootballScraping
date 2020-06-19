rawFile = input("FileName")
formattedFile = rawFile.split(" RAW")[0]
formattedFile = open(formattedFile,"w")
with open(rawFile,encoding="utf8") as f:
        content = f.readlines()
content = [x.strip() for x in content]

writtenToFile = 0
repeats = 0
leagueLinks = []

for c in content:
    if "#events" not in c and "/matches/2" in c:
        if(c in leagueLinks):   
            repeats+=1
        else:
            leagueLinks.append(c)
            writtenToFile +=1
            formattedFile.write(c + "\n")
    
print("Repeats: " + str(repeats))
print("WrittenToFile: " + str(writtenToFile))
print(len(leagueLinks)==writtenToFile)
