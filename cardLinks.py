import requests
from bs4 import BeautifulSoup




def cardLinksfunc():
    yellowCardLink = ""
    redCardLink = ""
    red2YCardLink = ""
    game1 = "https://us.soccerway.com/matches/2019/11/11/argentina/primera-division/club-atletico-velez-sarsfield/boca-juniors/3070465/?ICID=PL_MS_11"
    game2 = "https://us.soccerway.com/matches/2019/11/21/brazil/serie-b/sport-club-do-recife/associacao-atletica-ponte-preta/2988242/?ICID=PL_MS_04"
    r = requests.get(game1, timeout = 40)
    soup = BeautifulSoup(r.content, "html.parser")
    imgs = soup.findAll("img")
    for img in imgs:
        if("YC.png" in img['src']):
            yellowCardLink = img['src']
        if("RC.png" in img['src']):
            redCardLink = img['src']
        if("Y2C.png" in img['src']):
            red2YCardLink = img['src']
    r2 = requests.get(game2, timeout = 40)
    soup2 = BeautifulSoup(r2.content, "html.parser")
    imgs2 = soup2.findAll("img")
    for img in imgs2:
        if("YC.png" in img['src']):
            yellowCardLink = img['src']
        if("RC.png" in img['src']):
            redCardLink = img['src']
        if("Y2C.png" in img['src']):
            red2YCardLink = img['src']
    return yellowCardLink,redCardLink,red2YCardLink

yellowCardLink,redCardLink,red2YCardLink = cardLinksfunc()

print(yellowCardLink)
print(len(yellowCardLink))
print(redCardLink)
print(len(redCardLink))
print(red2YCardLink)
print(len(red2YCardLink))