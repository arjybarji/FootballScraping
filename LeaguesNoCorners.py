import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import uuid
import time
from multiprocessing import Pool
import sys, os
import urllib.request


def parse(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        }
        r = requests.get(url, timeout = 10,headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")
        dds = soup.findAll('dd')
        teams = soup.findAll('h3', attrs = {'class' : 'thick'})
        middle = teams[1].text.strip()
        if len(middle)> 0 and ':' not in middle:
            try:
                iframe = soup.findAll('iframe')
                iframeSrc = iframe[1]['src']
                url = 'https://us.soccerway.com/' + iframeSrc
                c = requests.get(url,timeout = 10)
                soupC = BeautifulSoup(c.content, "html.parser")
                cornerContainer = soupC.findAll('td', attrs = {'class' : 'legend left value'})
                homeCorners = cornerContainer[0].text.strip()
                print(dds[0].text.strip())
                return None
            except Exception as e:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                print(exc_type, fname, exc_tb.tb_lineno)
                print(dds[0].text.strip())
                return(dds[0].text.strip()+ "\n")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        return None

noCorners = open("NoCorners.txt","w")

with open('links.txt') as f:
    content = f.readlines()
content = [x.strip() for x in content]

if __name__ == '__main__':
    start_time = time.time()
    p = Pool(20)  # Pool tells how many at a time
    records = p.map(parse, content)
    p.terminate()
    p.join()
    for r in records:
        if r is not None:
            noCorners.write(r)
    print("--- %s seconds ---" % (time.time() - start_time))
