links = []
file = open('links.txt','w')

def getLinks(start,end):
    for i in range(start,end+1):
        leagueUrl = 'https://us.soccerway.com/matches/2018/08/10/england/premier-league/manchester-united-fc/leicester-city-fc/'
        file.write( leagueUrl +str(i)+'/' + "\n")
        
#Brasil Serie A
getLinks(2988916,2989295)
#Brasil Serie B
getLinks(2987874,2988253)
