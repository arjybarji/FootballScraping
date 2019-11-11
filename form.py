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
        isHome = True if len(soup.findAll('ul', attrs = {'id':'block_home_matches_30_subnav'})) > 0 else False
        if(isHome == False):
            teams = soup.findAll('h3', attrs = {'class' : 'thick'})
            homeTeam = teams[0].text.strip()
            awayTeam = teams[2].text.strip()
            
                        

                    print("Got Score. " + homeTeam + " vs " + awayTeam+" . " + gameWeek + " NO FRAME")
                    return("S$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + homeGoals + "," + awayGoals + "," + str(matchGoals) + "," + btts + "," + firstHalfHomeGoals + "," + firstHalfHomeConc + "," + firstHalfAwayGoals + "," + firstHalfAwayConc + "," + str(firstHalfTotalGoals) + "," + str(secondHalfHomeGoals) + "," + str(secondHalfHomeConc) + "," + str(secondHalfAwayGoals) + "," + str(secondHalfAwayConc) + "," + str(secondHalfTotalGoals) + "," + "" + "," + "" + "," + "" + "," + "" + "," + "" + "," + "" + "," + "" + "," + ""+","+dds[0].text.strip()+ "," + gameID)
            else:
                print(homeTeam + " vs " + awayTeam + " at " + middle + " GW:" + gameWeek + " Date: " + date)
                return("F$" + homeTeam + "," + awayTeam  + "," + gameWeek + "," + date + "," + dds[0].text.strip() + "," + gameID +  "£" + url)
        
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        #print(exc_type, fname, exc_tb.tb_lineno)
        #print(teams)
        #print(url)
        print(e)
        return("L$" + url + "\n")


with open('premlinks.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

if __name__ == '__main__':
    start_time = time.time()
    proxies = get_proxies()
    if(len(proxies)>0):
        p = Pool(40)  # Pool tells how many at a time
        records = p.map(parse, content)
        p.terminate()
        p.join()
        for r in records:
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
        print("Length of Records:" + str(len(content)))
        print("Stats: " + str(statsNum))
        print("Fixtures: " + str(fixturesNum))
        print("Errors:" + str(errorNum))
    
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)    
    print("--- %s minutes ---" % ((time.time() - start_time)/60))
