links = []
file = open('links.txt','w')
h2hfile = open('H2HLinks.txt','w')
#file = open('AllLinks.txt','w')

def getLinks(start,end):
    for i in range(start,end+1):
        leagueUrl = 'https://us.soccerway.com/matches/2018/08/10/england/premier-league/manchester-united-fc/leicester-city-fc/'
        file.write( leagueUrl +str(i)+'/' + "\n")
        h2hfile.write( leagueUrl +str(i)+'/' + "head2head/" +  "\n")

def getLinksFromFile(fileq):
    with open("LeagueLinks/" + fileq) as f:
        content = f.readlines()
    for c in content:
        c.strip()
        file.write(c)

#Premier League
getLinksFromFile("Premier League 1920")

#Championship
#getLinksFromFile()

#League One
#getLinksFromFile()

#League Two
#getLinksFromFile()

#National League
#getLinksFromFile()

#National League North and South
#getLinksFromFile()

#Scotland Premier
getLinksFromFile("Scotland Premier 2021")

#Scotland Championship
#getLinksFromFile()

#Scotland League One
#getLinksFromFile()

#Scotland League 2
#getLinksFromFile()

#Ireland
getLinksFromFile('Ireland 20')

#Wales
#getLinks(3042798,3042929)

#Serie A
getLinksFromFile('Serie A 1920')

#Serie B
getLinks(3122543,3122922)

#La Liga
#getLinksFromFile()

#Segunda Division
#getLinksFromFile()

#Bundesliga
#getLinksFromFile()

#2. Bundes
#getLinksFromFile()

#3. Bundesliga
#getLinksFromFile()

#Ligue1
#getLinksFromFile()

#Ligue 2
#getLinksFromFile()

#National 1 
#getLinksFromFile()

#Portugal League
getLinksFromFile("Portugal 1920")

#Segunda Liga
#getLinks(3065081,3065386)

#Eredivisie
#getLinksFromFile()

#Eerste Divisie
#getLinksFromFile()

#Austria
#getLinksFromFile()

#Austria 2
getLinksFromFile("Austria 2 1920")

#Denmark
#getLinksFromFile()

#Denmark1
getLinks(3034132,3034329)

#Norway - Only 16 out of 30 gameweeks
#Last day collected 30/08/20
getLinksFromFile("Norway 20")

#Norway 2
getLinksFromFile("Norway 2 20")

#Sweden 
getLinksFromFile("Sweden 20")

#Sweden 2
getLinksFromFile("Sweden 2 20")

#Finland
getLinksFromFile("Finland 20")

#Iceland
getLinksFromFile("Iceland 20")

#Belgium
#getLinksFromFile()

#Czech
#getLinksFromFile()

#Czech2
#getLinksFromFile()

#Croatia
getLinks(3029812,3029991)

#Poland
#getLinksFromFile()

#Poland2
getLinksFromFile("Poland 2 1920")

#Poland3
getLinksFromFile("Poland 3 1920")

#Russia
#getLinksFromFile()  

#Switzerland
getLinks(3037815,3037994)

#Swiss 2
getLinks(3039666,3039845)

#Turkey
getLinks(3081777,3082082)

#Turkey2
#getLinksFromFile()

#Greece
#getLinksFromFile()

#Romania
#getLinksFromFile()

#Slovakia
#getLinksFromFile()

#Slovenia
#getLinksFromFile()

#Serbia
#getLinksFromFile()

#Isreal League 
#getLinksFromFile()

#Hungary League 
#getLinksFromFile()

#Belarus
getLinksFromFile("Belarus 20")

#Brasil Serie A
#getLinks(,)

#Brasil Serie B
#getLinks(,)

#LigaMx
#Apertura
getLinksFromFile("Mexico Apertura 20")
#Clausera
#getLinks(3195272,3195424)

#Argentina
#getLinks(3070319,3070594)

#Bolivia
#Apertura
#getLinks(3212693,3212874)
#Clausera
#getLinks(,)

#Columbia
#Apertura
#getLinks(3206261,3206460)
#Clausera
#getLinks(,)

#China
#Only 14/30 gameweeks. Until 27/09/20
getLinksFromFile("CSL 2021")

#J1 League
getLinksFromFile("Japan 20")

#J2 League
getLinksFromFile("Japan 2 20")

#J3 League
getLinksFromFile("Japan 3 20")

#KLeague
getLinks(3269418,3269549)

#KLeague2
getLinks(3269283,3269417)

#Vietnam - Only 13 out of 26 gameweeks
getLinksFromFile("Vietnam 20")

#Egpyt
#getLinksFromFile()

#A-League
getLinks(3129271,3129413)

#MLS
#getLinksFromFile()

#getLinks(,)

'''
ToGet:
    
    '''