import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import uuid
import time
from multiprocessing import Pool
import sys, os
import urllib.request


with open('done.txt') as f:
    doneIDs = f.readlines()
doneIDs = [x.strip() for x in doneIDs]

def parse(url):
    gameID = url.split("/")[-2]
    if gameID not in doneIDs:
        try:
            #print(url)
            delays = [0.25,0.5,0.75,1]
            delay = np.random.choice(delays)
            time.sleep(delay)
            #r = requests.get(url)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            }
            r = requests.get(url, timeout = 20,headers=headers)
            if(r.status_code !=200):
                print(r.status_code)
            soup = BeautifulSoup(r.content, "html.parser")
            isHome = True if len(soup.findAll('ul', attrs = {'id':'block_home_matches_30_subnav'})) > 0 else False
            if(isHome == False):
                teams = soup.findAll('h3', attrs = {'class' : 'thick'})
                homeTeam = teams[0].text.strip()
                awayTeam = teams[2].text.strip()
                if(len(teams)!=3):
                    print(teams)
                middle = teams[1].text.strip()
                dds = soup.findAll('dd')
                date = dds[1].text.strip()
                gameWeek = dds[2].text.strip()
                if len(middle.split(" - "))>1:
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
                    won = ""
                    if(matchGoals<3):
                        won = "y"
                    if(matchGoals>3):
                        won = "n"
                    if(matchGoals==3):
                        won = "p"
                    print("Got Score . " + homeTeam + " vs " + awayTeam+" . " + gameWeek )
                    return("S$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + str(matchGoals) + "," + won +","+dds[0].text.strip() + "," + gameID)
                else:
                    print(homeTeam + " vs " + awayTeam + " at " + middle + " GW:" + gameWeek)
                    return("F$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + date + "£" + url)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            #print(teams)
            print(url)
            return("L$" + url + "\n")


stats = open('Statsv2.csv','a',encoding='utf-8')
fixtures = open('fixturesv2.csv','w',encoding='utf-8')

with open('links.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

links = open('links.txt','r')
errors = open('errors.txt','w')
done = open('done.txt','a')

if __name__ == '__main__':
    start_time = time.time()
    p = Pool(10)  # Pool tells how many at a time
    records = p.map(parse, content)
    p.terminate()
    p.join()
    errorNum = 0
    fixturesNum = 0
    statsNum = 0
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
    print("Length of Records:" + str(len(records)))
    print("Stats: " + str(statsNum))
    print("Fixtures: " + str(fixturesNum))
    print("Errors:" + str(errorNum))
    print("--- %s seconds ---" % (time.time() - start_time))
    input()
