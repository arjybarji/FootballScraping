a = "19 January 2020"
b = "2 February 2020"

import datetime

today = datetime.date.today()
days = []
tocheck = []
days.append(today)
for i in range(1,365):
    days.append(datetime.date.today() + datetime.timedelta(days=i))
for d in days:
    s = str(d).split("-")
    if s[2].startswith("0"):
        day = s[2].split("0")[1]
    else:
        day = s[2]
    if s[1].startswith("0"):
        month = s[1].split("0")[1]
    else:
        month = s[1]
    month = datetime.date(1900, int(month), 1).strftime('%B')
    year = s[0]
   
    tocheck.append(day + " " + month + " " + year)

with open('fixturesv2.csv',encoding="utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content]

for i in content:
    if i.split(",")[3] not in tocheck:
        print(i)