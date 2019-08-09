links = []
file = open('links.txt','a')

def getLinks(start,end):
    for i in range(start,end+1):
        leagueUrl = 'https://us.soccerway.com/matches/2018/08/10/england/premier-league/manchester-united-fc/leicester-city-fc/'
        file.write( leagueUrl +str(i)+'/' + "\n")
for j in range(0,19):
    if(j == 0):
        #Premier
        getLinks(2795269,2795649)
    elif(j == 1):
        #Serie A
        getLinks(2863757,2864136)
    elif(j == 2):
        #Eredivisie
        getLinks(2793927,2794232)
    elif(j == 3):
        #English Lower Leagues
        getLinks(2801007,2802664)
    elif (j==4):
        #La Liga
        getLinks(2857020,2857399)
    elif (j==5):
        #Ligue1
        getLinks(2792216,2792595)
    elif (j==6):
        #Bundesliga
        getLinks(2810909,2811214)
    elif (j==7):
        #Portugal League
        getLinks(2825904,2826209)
    elif (j==8):
        #National League
        getLinks(2817368,2817919)
    elif (j==9):
        #Eerste Divisie
        getLinks(2794371,2794750)
    elif (j==10):
        #2. Bundes
        getLinks(2811216,2811521)
    elif (j==11):
        # Serie B
        getLinks(2893670,2894011)
    elif (j==12):
        #Ligue 2
        getLinks(2792596,2792975)
    elif (j==13):
        #Segunda Liga
        getLinks(2826210,2826515)
    elif (j==14):
        # Segunda Division
        getLinks(2861541,2862018)
    elif (j==15):
        #Scotland Premier
        getLinks(2796275,2796472)
    elif (j==16):
        #Scotland Championship
        getLinks(2796095,2796274)
    elif (j==17):
        #A-League
        getLinks(2834919,2835053)
    elif (j==18):
        #Saudi League
        getLinks(2830302,2830541)
