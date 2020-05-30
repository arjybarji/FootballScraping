rawFile = "Belarus 2020 RAW"
formattedFile = rawFile.split(" RAW")[0]
formattedFile = open(formattedFile,"w")
with open(rawFile,encoding="utf8") as f:
        content = f.readlines()
content = [x.strip() for x in content]

for c in content:
    if "#events" not in c:
        formattedFile.write(c + "\n")
    

