import requests
from bs4 import BeautifulSoup

page = "https://us.soccerway.com/matches/2019/12/07/italy/serie-a/ss-lazio-roma/juventus-fc/3111843/"
page2 = "https://us.soccerway.com/matches/2019/12/08/italy/serie-a/us-lecce/genoa-cfc/3111844/"

yellowCardLink = "https://s1.swimg.net/gsmf/757/img/events/YC.png"
redCardLink = "https://s1.swimg.net/gsmf/757/img/events/RC.png"
red2YCardLink = "https://s1.swimg.net/gsmf/757/img/events/Y2C.png"

def get(url):
    r = requests.get(url, timeout = 40)
    if(r.status_code !=200):
        print(r.status_code)
    soup = BeautifulSoup(r.content, "html.parser")
    teams = soup.findAll('h3', attrs = {'class' : 'thick'})
    homeTeam = teams[0].text.strip()
    awayTeam = teams[2].text.strip()
    print(homeTeam  + " vs " + awayTeam )
    try:   
        homeTeamCards = 0                       
        homeTeamContainers = soup.findAll('div', attrs = {'class' : 'container left'})
        homeTeamImgs = []
        for htcI in homeTeamContainers[2].findAll('img'):
            homeTeamImgs.append(htcI)
        for htcI in homeTeamContainers[3].findAll('img'):
            homeTeamImgs.append(htcI)
        for htc in homeTeamImgs:
            if("YC.png" in htc['src'] or "RC.png" in htc['src'] or "Y2C.png" in htc['src']):
                homeTeamCards+=1
        
        awayTeamCards = 0
        awayTeamContainers = soup.findAll('div', attrs = {'class' : 'container right'})
        awayTeamImgs = []
        for atcI in awayTeamContainers[2].findAll('img'):
            awayTeamImgs.append(atcI)
        for atcI in awayTeamContainers[3].findAll('img'):
            awayTeamImgs.append(atcI)
        for atc in awayTeamImgs:
            if("YC.png" in atc['src'] or "RC.png" in atc['src'] or "Y2C.png" in atc['src']):
                awayTeamCards+=1

        matchCards = homeTeamCards + awayTeamCards
        print(homeTeamCards)
        print(awayTeamCards)
        print(matchCards)
    except Exception as e:
        print(e)
        homeTeamCards = -1
        awayTeamCards = -1
        matchCards = -1

get(page)
get(page2)                        