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
import datetime


today = datetime.date.today().strftime("%B").lower()
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

def replaceTeam(team,league):
    if(team == "Arsenal"):
        team = team + " - " + league
    return team    

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
                if(r.status_code == 404):
                    print("Not Found Error")
                if(r.status_code == 503):
                    print("Service Unavailable Error")
            soup = BeautifulSoup(r.content, "html.parser")
            #Check if page is valid
            isHome = True if len(soup.findAll('ul', attrs = {'id':'block_home_matches_28_subnav'})) > 0 else False
            if(isHome == False):
                #Get Teams
                teams = soup.findAll('a', attrs = {'class' : 'team-title'})
                #teams = soup.findAll('a', attrs = {'class' : 'team-title'})
                homeTeam = teams[0].text.strip()
                awayTeam = teams[1].text.strip()
                if(len(teams)!=2):
                    print(teams)
                    
                #Check if postponed
                postponed = soup.findAll('span',attrs = {'class':'details postponed'})
                if(len(postponed)>0):
                    #print("Postponed")
                    return None
                
                #Get game info section
                gameInfo = soup.findAll('div',attrs = {'class':'details'})
                date = gameInfo[0].findAll('a')[0].text.strip()
                #print(date)
                league = gameInfo[0].findAll('a')[1].text.strip()
                #print(league)
                gameWeek = gameInfo[0].findAll('span')[3].text.strip()
                #print(gameWeek)
                dateT = str(datetime.datetime.strptime(date, '%d/%m/%Y').date())
                
                #League Convert
                country = soup.findAll('h2',attrs={'class':'header-label'})[0].text.strip().capitalize()
                league = league + " - " + country
                #print(league)
                homeTeam = replaceTeam(homeTeam,league)
                awayTeam = replaceTeam(awayTeam,league)
                '''
                try:
                    gameWeek = int(dds[2].text.strip().replace(",",""))
                except:
                    gameWeek = 0
                '''
                gameWeek = str(gameWeek)
                
                scoreTime = soup.findAll('h3',attrs = {'class':'thick scoretime'})[0]
                scoreTimeText = scoreTime.text
                if ':' not in scoreTimeText and len(scoreTimeText.strip())>0:
                    scoreSplit = scoreTimeText.split("\n")
                    fullTime = scoreSplit[3].strip()
                    halfTime = scoreSplit[9].strip().replace("(","").replace(")","").replace("HT","").strip()
                    #scoreTime = scoreTime.split(" - ")
                    homeGoals = 0
                    awayGoals = 0
                    homeGoals = fullTime.split(" - ")[0]
                    awayGoals = fullTime.split(" - ")[1]
                    matchGoals = int(homeGoals) + int(awayGoals)
                    if(matchGoals >= 0):
                        if(int(homeGoals) > 0 and int(awayGoals) > 0):
                            btts = "y"
                        else:
                            btts = "n"
                        halfTimeScore = halfTime.split(" - ")
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
                            
                            homeTeamCards = 0                       
                            homeTeamContainers = soup.findAll('div', attrs = {'class' : 'container left'})
                            homeTeamImgs = []
                            for htcI in homeTeamContainers[1].findAll('img'):
                                homeTeamImgs.append(htcI)
                            for htcI in homeTeamContainers[2].findAll('img'):
                                homeTeamImgs.append(htcI)
                            for htc in homeTeamImgs:
                                if("YC.png" in htc['src'] or "Y2C.png" in htc['src']):
                                    homeTeamCards+=1
                                if("RC.png" in htc['src']):
                                    homeTeamCards+=2
        
                            awayTeamCards = 0
                            awayTeamContainers = soup.findAll('div', attrs = {'class' : 'container right'})
                            awayTeamImgs = []
                            for atcI in awayTeamContainers[1].findAll('img'):
                                awayTeamImgs.append(atcI)
                            for atcI in awayTeamContainers[2].findAll('img'):
                                awayTeamImgs.append(atcI)
                            for atc in awayTeamImgs:
                                if("YC.png" in atc['src'] or "Y2C.png" in atc['src']):
                                    awayTeamCards+=1
                                if("RC.png" in atc['src']):
                                    awayTeamCards+=2

                            matchCards = homeTeamCards + awayTeamCards

                        except Exception as e:
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
                            homeCorners = cornerContainer[1].text.strip()
                            awayCornersConc = homeCorners
                            cornerContainer = soupC.findAll('td', attrs = {'class' : 'legend right value'})
                            awayCorners = cornerContainer[1].text.strip()
                            homeCornersConc = awayCorners
                            matchCorners = int(homeCorners) + int(awayCorners)

                            print("GOT SCORE . " + homeTeam + " vs " + awayTeam+" . " + dateT )
                            return("S$" + homeTeam + "," + awayTeam  + "," + dateT + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + str(homeTeamCards) + "," + str(awayTeamCards) + "," + str(matchCards) + "," + homeCorners + "," + awayCorners + "," + homeCornersConc + "," + awayCornersConc + "," + str(matchCorners)+","+league + "," + gameID)
                        except Exception as e:
                            exc_type, exc_obj, exc_tb = sys.exc_info()
                            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                            print("GOT SCORE no corners. " + homeTeam + " vs " + awayTeam+" . " + dateT + " NO FRAME")
                            return("S$" + homeTeam + "," + awayTeam  + "," + dateT + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + str(homeTeamCards) + "," + str(awayTeamCards) + "," + str(matchCards) + "," + "-1" + "," + "-1" + "," + "-1" + "," + "-1" + "," + "-1"+","+league+ "," + gameID)
                else:
                    dateDay = int(date.lower().split("/")[0])
                    check = int(datetime.datetime.today().day)
                    if(today in date.lower() and dateDay < (check+1)):
                        print(homeTeam + " vs " + awayTeam + " at " + middle + " GW:" + gameWeek + " Date: " + date)                    
                    return("F$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + date + "," + league + "," + gameID +  "£" + url)
        
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            #print(teams)
            print(url)
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
        #p = Pool(80)  # Pool tells how many at a time
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
