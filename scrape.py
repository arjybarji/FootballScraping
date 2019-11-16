import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import uuid
import time
from multiprocessing import Pool
import sys, os
import urllib.request
import requests
from lxml.html import fromstring
import random
from itertools import cycle
import winsound


with open('done.txt') as f:
    doneIDs = f.readlines()
doneIDs = [x.strip() for x in doneIDs]

def get_proxies():
    url = 'https://free-proxy-list.net/'
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:100000]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies
proxies = get_proxies()

def parse(url):
    gameID = url.split("/")[-2]
    if gameID not in doneIDs:
        try:
            #print(url)
            delays = [2,3,4,5,6,7]
            delay = np.random.choice(delays)
            time.sleep(delay)
            user_agent_list = [
               #Chrome
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                #Firefox
                'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
                'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
                'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
            ]
            user_agent = random.choice(user_agent_list)
            proxy = random.choice(list(proxies))
            headers = {'User-Agent': user_agent}
            r = requests.get(url, timeout = 40,headers=headers,proxies={"http": proxy})
            if(r.status_code !=200):
                print(r.status_code)
            soup = BeautifulSoup(r.content, "html.parser")
            isHome = True if len(soup.findAll('ul', attrs = {'id':'block_home_matches_28_subnav'})) > 0 else False
            if(isHome == False):
                teams = soup.findAll('h3', attrs = {'class' : 'thick'})
                homeTeam = teams[0].text.strip()
                awayTeam = teams[2].text.strip()
                if(len(teams)!=3):
                    print(teams)
                middle = teams[1].text.strip()
                dds = soup.findAll('dd')
                dts = soup.findAll('dt')
                date = dds[1].text.strip()
                league = dds[0].text.strip()
                #print(soup.findAll('div', attrs = {'class' : 'block  clearfix block_competition_left_tree-wrapper'}))
                country = dds[0].find('a')['href'].split("/")[2].strip().capitalize()
                league = league + " - " + country
                kickOff = False
                for c in dts:
                    if(c.text.strip() == "Kick-off"):
                        kickOff = True
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
                        if(kickOff):
                            halfTimeScore = dds[4].text.strip().split(" - ")
                        else:
                            halfTimeScore = dds[3].text.strip().split(" - ")
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
                        
                        try:
                            homeTeamContainers = soup.findAll('div', attrs = {'class' : 'container left'})
                            homeTeamStarting = homeTeamContainers[2]
                            homeTeamBench = homeTeamContainers[3]
                            homeTeamYellows = len(homeTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/YC.png' })) + len(homeTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/YC.png' }))
                            homeTeamReds = len(homeTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/RC.png' })) + len(homeTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/RC.png' })) + len(homeTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/Y2C.png' })) + len(homeTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/Y2C.png' }))
                            homeTeamCards = homeTeamYellows + homeTeamReds

                            awayTeamContainers = soup.findAll('div', attrs = {'class' : 'container right'})
                            awayTeamStarting = awayTeamContainers[2]
                            awayTeamBench = awayTeamContainers[3]
                            awayTeamYellows = len(awayTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/YC.png' })) + len(awayTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/YC.png' }))
                            awayTeamReds = len(awayTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/RC.png' })) + len(awayTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/RC.png' })) + len(awayTeamStarting.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/Y2C.png' })) + len(awayTeamBench.findAll('img', attrs = {'src' : 'https://s1.swimg.net/gsmf/741/img/events/Y2C.png' }))
                            awayTeamCards = awayTeamYellows + awayTeamReds

                            matchCards = homeTeamCards + awayTeamCards
                        except Exception:
                            homeTeamCards = -1
                            awayTeamCards = -1
                            matchCards = -1
                        try:
                            iframe = soup.findAll('iframe')[-1]
                            iframeSrc = iframe['src']
                            url = 'https://us.soccerway.com/' + iframeSrc
                            
                            c = requests.get(url,timeout = 40,headers=headers)
                            soupC = BeautifulSoup(c.content, "html.parser")

                            cornerContainer = soupC.findAll('td', attrs = {'class' : 'legend left value'})
                            homeCorners = cornerContainer[0].text.strip()
                            awayCornersConc = homeCorners
                            cornerContainer = soupC.findAll('td', attrs = {'class' : 'legend right value'})
                            awayCorners = cornerContainer[0].text.strip()
                            homeCornersConc = awayCorners
                            matchCorners = int(homeCorners) + int(awayCorners)

                            print("Got Score . " + homeTeam + " vs " + awayTeam+" . " + gameWeek )
                            return("S$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + str(homeTeamCards) + "," + str(awayTeamCards) + "," + str(matchCards) + "," + homeCorners + "," + awayCorners + "," + homeCornersConc + "," + awayCornersConc + "," + str(matchCorners)+","+league + "," + gameID)
                        except Exception as e:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            print("Got Score no corners. " + homeTeam + " vs " + awayTeam+" . " + gameWeek + " NO FRAME")
                            return("S$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + str(homeTeamCards) + "," + str(awayTeamCards) + "," + str(matchCards) + "," + "-1" + "," + "-1" + "," + "-1" + "," + "-1" + "," + "-1"+","+league+ "," + gameID)
                else:
                    print(homeTeam + " vs " + awayTeam + " at " + middle + " GW:" + gameWeek + " Date: " + date)
                    return("F$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + date + "," + league + "," + gameID +  "£" + url)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            #print(exc_type, fname, exc_tb.tb_lineno)
            #print(teams)
            #print(url)
            print(e)
            return("L$" + url + "\n")


stats = open('Statsv2.csv','a',encoding='utf-8')


with open('links.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

links = open('links.txt','r')
errors = open('errors.txt','w')
done = open('done.txt','a')

if __name__ == '__main__':
    start_time = time.time()
    proxies = get_proxies()
    todo = []
    for c in content:
        gameID = c.split("/")[-2]
        if gameID not in doneIDs:
            todo.append(c)
    print(len(proxies))
    if(len(proxies)>0):
        p = Pool(50)  # Pool tells how many at a time
        records = p.map(parse, todo)
        p.terminate()
        p.join()
        errorNum = 0
        fixturesNum = 0
        statsNum = 0
        fixtures = open('fixturesv2.csv','w',encoding='utf-8')
        for r in records:
            #print(r)
            if r is not None:
                if r[0] == "S":
                    splitted = r.split("$")
                    stats.write(splitted[1] + "\n")
                    gameIDW = splitted[1].split(",")[-1]
                    done.write(gameIDW + "\n")
                    statsNum = statsNum+1
                if r[0] == "F":
                    splitted = r.split("$")
                    splitted2 = splitted[1].split("£")
                    fixtures.write(splitted2[0] + "\n")
                    #links.write(splitted2[1] + "\n")
                    fixturesNum = fixturesNum+1
                if r[0] == "L":
                    splitted = r.split("$")
                    #links.write(splitted[1])
                    errors.write(splitted[1])
                    errorNum = errorNum+1
        print("Length of Records:" + str(len(todo)))
        print("Stats: " + str(statsNum))
        print("Fixtures: " + str(fixturesNum))
        print("Errors:" + str(errorNum))
    
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)    
    print("--- %s minutes ---" % ((time.time() - start_time)/60))
