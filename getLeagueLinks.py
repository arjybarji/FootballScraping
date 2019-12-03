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

start = 3028914
end = 3032887
toCheck = "First League - Bulgaria"
leagueFile = open(toCheck + " - Links.txt","w")

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

def check(value):
    leagueUrl = 'https://us.soccerway.com/matches/2018/08/10/england/premier-league/manchester-united-fc/leicester-city-fc/'
    gameURL = leagueUrl +str(value)+'/'
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
    r = requests.get(gameURL, timeout = 40,headers=headers,proxies={"http": proxy})
    soup = BeautifulSoup(r.content, "html.parser")
    isHome = True if len(soup.findAll('ul', attrs = {'id':'block_home_matches_28_subnav'})) > 0 else False
    if(isHome == False):
        try:
            dds = soup.findAll('dd')
            league = dds[0].text.strip()
            country = dds[0].find('a')['href'].split("/")[2].strip().capitalize()
            league = league + " - " + country
            print(end - value)
            if(league == toCheck):
                return(gameURL)
        except Exception as e:
            print(e)
        
        
if __name__ == '__main__':
    start_time = time.time()
    proxies = get_proxies()
    todo = range(start,end+1)
    if(len(proxies)>0):
        #p = Pool(50)  # Pool tells how many at a time
        p = Pool(30)  # Pool tells how many at a time
        records = p.map(check, todo)
        p.terminate()
        p.join()
        for r in records:
            if r is not None:
                print(r)
                leagueFile.write(r + "\n")
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)    
    print("--- %s minutes ---" % ((time.time() - start_time)/60))

    