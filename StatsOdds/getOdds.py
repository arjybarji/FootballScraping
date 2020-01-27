import requests
from bs4 import BeautifulSoup
import uuid

#years = ["2004-2005","2005-2006","2006-2007","2007-2008","2008-2009","2009-2010","2010-2011","2011-2012","2012-2013","2013-2014","2014-2015","2015-2016","2016-2017","2017-2018","2018-2019"]
years = ["2004-2005"]
for year in years:
    count = 0
    for i in range(1,2):
        url = "https://www.oddsportal.com/soccer/england/premier-league-"+year+"/results/#/page/" + str(i)+"/"
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser",)
        print(soup)
        print(soup.findAll('div', attrs = {'id':'tournamentTable'}))