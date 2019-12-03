with open("Statsv2.csv","r",encoding = "utf8") as f:
    content = f.readlines()
content = [x.strip() for x in content]

def commonScores():
    scores = dict()
    for c in content:
        homeGoals = c.split(",")[3]
        awayGoals = c.split(",")[4]
        score = homeGoals+"-"+awayGoals
        if(score not in scores) and (score[::-1] in scores):
            scores.update({score : scores[score[::-1]]})
        if(score not in scores):
            scores.update({score : 0})
        scores.update({score:scores[score]+1})
    return scores

d = commonScores()
for c in d:
    print(c + " Num:"+str(d[c]))