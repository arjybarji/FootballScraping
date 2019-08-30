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
        print(homeTeam)
        return homeTeam
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return None


teams = open('teams.csv','w',encoding='utf-8')


with open('AllLinks.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

if __name__ == '__main__':
    start_time = time.time()
    p = Pool(30)  # Pool tells how many at a time
    records = p.map(parse, content)
    p.terminate()
    p.join()
    teamsA = []
    print(len(records))
    for r in records:
        if r is not None:
            if r not in teamsA:
                teams.write(r + "\n")
                teamsA.append(r)			
    print("--- %s seconds ---" % (time.time() - start_time))

