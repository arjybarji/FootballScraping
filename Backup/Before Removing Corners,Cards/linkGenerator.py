links = []
file = open('links.txt','w')
#file = open('AllLinks.txt','w')

def getLinks(start,end):
    for i in range(start,end+1):
        leagueUrl = 'https://us.soccerway.com/matches/2018/08/10/england/premier-league/manchester-united-fc/leicester-city-fc/'
        file.write( leagueUrl +str(i)+'/' + "\n")

#Premier League
getLinks(3029073,3029452)
#Serie A
getLinks(3111700,3112079)
#La Liga
getLinks(3058810,3059189)
#Ligue1
getLinks(3030547,3030926)
#Bundesliga
getLinks(3047020,3047325)
#A-League
getLinks(3129271,3129413)

