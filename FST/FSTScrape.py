import requests
from bs4 import BeautifulSoup
import csv
import sys, os

url = "https://www.freesupertips.com/typeofbet/botd/"
betsurl = "https://www.freesupertips.com/tips/bet-of-the-day-"

rb = requests.get(url)
souprb = BeautifulSoup(rb.content, "html.parser")
maxi = souprb.find('a',attrs = {'class':'NewsItem'})
intMax = int(maxi.get('href').split("-")[-1].split("/")[0])

bets = open('bets.csv','w')

for i in range(0,intMax+1):
    r = requests.get(betsurl + str(i))
    soup = BeautifulSoup(r.content, "html.parser")
    try:
        tip = soup.findAll('div', attrs = {'class':'TipBetslip__market'})
        tip2 = soup.findAll('div', attrs = {'class':'TipBetslip__outcome'})
        returns = soup.findAll('span', attrs = {'class':'StakeSelector__tipped-at-returns'})[0].text.strip().split("£")[-1]
        odds = round(float(returns)/20, 2)
        tipfull = tip[0].text.strip() + " " + tip2[0].text.strip()
        print(tipfull + " at odds: " + str(odds))
        bets.write(tipfull + "," + str(odds)+"\n")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)


input("Done")