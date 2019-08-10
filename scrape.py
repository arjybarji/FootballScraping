import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import uuid
import time
from multiprocessing import Pool
import sys, os


def parse(url):
    try:
        #print(url)
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
        date = dds[1].text.strip()
        gameWeek = dds[2].text.strip()
        if ':' not in middle:
            middle = middle.split(" - ")
            homeGoals = 0
            awayGoals = 0
            homeGoals = middle[0]
            try:
                awayGoals = middle[1]
            except Exception as e:
                homeGoals = "-1"
                awayGoals = "-1"
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

                    print("Got Score . " + homeTeam + " vs " + awayTeam+" . " + gameWeek )
                    return("S$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + str(homeTeamCards) + "," + str(awayTeamCards) + "," + str(matchCards) + "," + homeCorners + "," + awayCorners + "," + homeCornersConc + "," + awayCornersConc + "," + str(matchCorners)+","+dds[0].text.strip() + "\n")
                except Exception as e:
                    print("Got Score no corners. " + homeTeam + " vs " + awayTeam+" . " + gameWeek + " NO FRAME")
                    return("S$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + str(homeTeamCards) + "," + str(awayTeamCards) + "," + str(matchCards) + "," + "" + "," + "" + "," + "" + "," + "" + "," + ""+","+dds[0].text.strip() + "\n")
        else:
            print(homeTeam + " vs " + awayTeam + " at " + middle + " GW:" + gameWeek)
            return("F$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + date + "£" + url)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(url)
        return("L$" + url + "\n")


stats = open('Statsv2.csv','a',encoding='utf-8')
fixtures = open('fixturesv2.csv','w',encoding='utf-8')

with open('links.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

links = open('links.txt','w')

if __name__ == '__main__':
    start_time = time.time()
    p = Pool(20)  # Pool tells how many at a time
    records = p.map(parse, content)
    p.terminate()
    p.join()
    print(len(records))
    for r in records:
        print(r)
        if r is not None:
            if r[0] == "S":
                splitted = r.split("$")
                stats.write(splitted[1])
            if r[0] == "F":
                splitted = r.split("$")
                splitted2 = splitted[1].split("£")
                fixtures.write(splitted2[0] + "\n")
                links.write(splitted2[1] + "\n")
            if r[0] == "L":
                splitted = r.split("$")
                links.write(splitted[1])
    print("--- %s seconds ---" % (time.time() - start_time))

'''
for url in content:
    parse(url)
'''
