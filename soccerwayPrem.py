import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import uuid
import time
from multiprocessing import Pool

def parse(url):
    try:
        delays = [0.25,0.5,0.75,1]
        delay = np.random.choice(delays)
        #time.sleep(delay)
        #r = requests.get(url)
        r = requests.get(url, timeout = 10)
        soup = BeautifulSoup(r.content, "html.parser")
        teams = soup.findAll('h3', attrs = {'class' : 'thick'})
        homeTeam = teams[0].text.strip()
        awayTeam = teams[2].text.strip()
        middle = teams[1].text.strip()
        dds = soup.findAll('dd')
        gameWeek = dds[2].text.strip()
        if ':' not in middle and dds[0].text.strip() in strips:
            #if(int(gameWeek) > lastGameWeek):
            #    break
            #print(middle)
            middle = middle.split(" - ")
            homeGoals = 0
            awayGoals = 0
            homeGoals = middle[0]
            try:
                awayGoals = middle[1]
            except Exception as e:
                homeGoals = "-1"
                awayGoals = "-1"
            #print(homeTeam + " " + homeGoals + " - " + awayGoals + " " + awayTeam)
            matchGoals = int(homeGoals) + int(awayGoals)
            if(matchGoals >= 0):
                if(int(homeGoals) > 0 and int(awayGoals) > 0):
                    btts = "y"
                else:
                    btts = "n"
                halfTimeScore = dds[4].text.strip().split(" - ")
                firstHalfHomeGoals = halfTimeScore[0]
                firstHalfAwayConc = halfTimeScore[0]
                firstHalfAwayGoals = halfTimeScore[1]
                firstHalfHomeConc = halfTimeScore[1]
                firstHalfTotalGoals = int(firstHalfHomeGoals) + int(firstHalfAwayGoals)
                secondHalfHomeGoals = int(homeGoals) - int(firstHalfHomeGoals)
                secondHalfAwayConc = int(homeGoals) - int(firstHalfHomeGoals)
                secondHalfAwayGoals = int(awayGoals) - int(firstHalfAwayGoals)
                secondHalfHomeConc = int(awayGoals) - int(firstHalfAwayGoals)
                secondHalfTotalGoals = matchGoals - firstHalfTotalGoals

                homeTeamContainers = soup.findAll('div', attrs = {'class' : 'container left'})
                homeTeamStarting = homeTeamContainers[2]
                homeTeamBench = homeTeamContainers[3]
                homeTeamYellows = len(homeTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/700/img/events/YC.png' })) + len(homeTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/699/img/events/YC.png' }))
                homeTeamReds = len(homeTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/700/img/events/RC.png' })) + len(homeTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/699/img/events/RC.png' }))
                homeTeamCards = homeTeamYellows + homeTeamReds

                awayTeamContainers = soup.findAll('div', attrs = {'class' : 'container right'})
                awayTeamStarting = awayTeamContainers[2]
                awayTeamBench = awayTeamContainers[3]
                awayTeamYellows = len(awayTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/700/img/events/YC.png' })) + len(awayTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/699/img/events/YC.png' }))
                awayTeamReds = len(awayTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/700/img/events/RC.png' })) + len(awayTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/699/img/events/RC.png' }))
                awayTeamCards = awayTeamYellows + awayTeamReds

                matchCards = homeTeamCards + awayTeamCards
                try:
                    iframe = soup.findAll('iframe')
                    iframeSrc = iframe[1]['src']
                    url = 'https://us.soccerway.com/' + iframeSrc
                    c = requests.get(url,timeout = 10)
                    soupC = BeautifulSoup(c.content, "html.parser")

                    cornerContainer = soupC.findAll('td', attrs = {'class' : 'legend left value'})
                    homeCorners = cornerContainer[0].text.strip()
                    awayCornersConc = homeCorners
                    cornerContainer = soupC.findAll('td', attrs = {'class' : 'legend right value'})
                    awayCorners = cornerContainer[0].text.strip()
                    homeCornersConc = awayCorners
                    matchCorners = int(homeCorners) + int(awayCorners)

                    print("To file . " + homeTeam + " vs " + awayTeam+" . " + gameWeek )
                    return(homeTeam + "," + awayTeam  + "," + gameWeek + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + str(homeTeamCards) + "," + str(awayTeamCards) + "," + str(matchCards) + "," + homeCorners + "," + awayCorners + "," + homeCornersConc + "," + awayCornersConc + "," + str(matchCorners)+","+dds[0].text.strip())
                except Exception as e:
                    print("To file . " + homeTeam + " vs " + awayTeam+" . " + gameWeek + " NO FRAME")
                    return(homeTeam + "," + awayTeam  + "," + gameWeek + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + str(homeTeamCards) + "," + str(awayTeamCards) + "," + str(matchCards) + "," + "" + "," + "" + "," + "" + "," + "" + "," + ""+","+dds[0].text.strip())

        else:
            print(homeTeam + " vs " + awayTeam + " at " + middle)
    except Exception as e:
        print(e)
        print(url)


file = open('StatsToPaste.csv','a',encoding='utf-8')

strips = ["Premier League","Serie A","Eredivisie", "Championship", "League One", "League Two", "Primeira Liga", "Bundesliga", "La Liga", "Ligue 1" , "National League" , "Eerste Divisie",
"2. Bundesliga","Serie B","Ligue 2","Segunda Liga","Segunda División","Premiership","Championship", "A-League" , "Eerste Divisie", "Pro League"]
with open('links.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]
if __name__ == '__main__':
    start_time = time.time()
    
    p = Pool(75)  # Pool tells how many at a time
    records = p.map(parse, content)
    p.terminate()
    p.join()
    print(len(records))
    for r in records:
        print(r)
        if r is not None:
            file.write(r + "\n")
    
    print("--- %s seconds ---" % (time.time() - start_time))
