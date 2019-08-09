import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import uuid
from multiprocessing import Pool
import time

def parse(url):
    delays = [0.25,0.5,0.75,1]
    delay = np.random.choice(delays)
    #time.sleep(delay)
    r = requests.get(url, timeout = 30)
    soup = BeautifulSoup(r.content, "html.parser")
    teams = soup.findAll('h3', attrs = {'class' : 'thick'})
    try:
        homeTeam = teams[0].text.strip()
        awayTeam = teams[2].text.strip()
        middle = teams[1].text.strip()
        dds = soup.findAll('dd')
        gameWeek = dds[2].text.strip()
        date = dds[1].text.strip()
        #print(date)
        #print(middle)
        #print(dds[0].text.strip())
        #print(gameWeek)
        if ':' in middle:
            print(homeTeam + "," + awayTeam  + "," + gameWeek + "," + date)
            return homeTeam + "," + awayTeam  + "," + gameWeek + "," + date
        else:
            print("Wrong Gameweek " + homeTeam + "," + awayTeam )
            return None
    except Exception as e:
        print(url)

'''
userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
headers = {
        'user-agent': userAgent
    }
'''

strips = ["Premier League","Serie A","Eredivisie", "Championship", "League One", "League Two", "Primeira Liga", "Bundesliga", "La Liga", "Ligue 1" , "National League" , "Eerste Divisie",
"2. Bundesliga","Serie B","Ligue 2","Segunda Liga","Segunda División","Premiership","Championship", "A-League" , "Eerste Divisie", "Pro League"]

file = open('FixturesToPaste.csv','a', encoding='utf-8')

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
