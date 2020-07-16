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
getLinksFromFile("Championship 1920")

#League One
#getLinksFromFile()

#League Two
#getLinksFromFile()

#National League
#getLinks(3053879,3054430)

#National League North and South
#getLinks(3054487,3055410)

#Scotland Premier
#getLinks(3038361,3038558)

#Scotland Championship
#getLinks(3038559,3038738)

#Scotland League One
#getLinks(3038181,3038360)

#Scotland League 2
#getLinks(3038739,3038918)

#Ireland
#getLinks(3197111,3197290)

#Wales
#getLinks(3042798,3042929)

#Serie A
getLinksFromFile('Serie A 1920')

#Serie B
getLinks(3122543,3122922)

#La Liga
getLinksFromFile("La Liga 1920")

#Segunda Division
getLinks(3059913,3060374)
#Do a getLinks

#Bundesliga
getLinks(3047020,3047325)

#2. Bundes
getLinks(3047327,3047632)

#3. Bundesliga
getLinks(3053138,3053517)

#Ligue1
#getLinks(3030547,3030926)

#Ligue 2
#getLinks(3031016,3031395)

#National 1 
#getLinks(3073147,3073452)

#Portugal League
getLinksFromFile("Portugal 1920")

#Segunda Liga
#getLinks(3065081,3065386)

#Eredivisie
#getLinks(3032053,3032358)

#Eerste Divisie
#getLinks(3031673,3032052)

#Austria
getLinks(3034837,3034968)

#Austria 2
getLinksFromFile("Austria 2 1920")

#Denmark
getLinks(3026880,3027061)

#Denmark1
getLinks(3034132,3034329)

#Norway - Only 16 out of 30 gameweeks
#Last day collected 30/08/20
getLinksFromFile("Norway 20")

#Sweden 
getLinksFromFile("Sweden 20")

#Sweden 2
getLinksFromFile("Sweden 2 20")

#Finland
getLinksFromFile("Finland 20")

#Iceland
getLinksFromFile("Iceland 20")

#Belgium
#getLinks(3050137,3050387)

#Czech
getLinks(3036786,3037025)

#Czech2
getLinks(3039244,3039483)

#Croatia
getLinks(3029812,3029991)

#Poland
getLinks(3025700,3025939)

#Poland2
getLinksFromFile("Poland 2 1920")

#Poland3
getLinksFromFile("Poland 3 1920")

#Russia
getLinks(3027073,3027312)       

#Switzerland
getLinks(3037815,3037994)

#Swiss 2
getLinks(3039666,3039845)

#Turkey
getLinks(3081777,3082082)

#Turkey2
getLinks(3083169,3083474)

#Greece
#getLinks(3051869,3052050)

#Romania
getLinks(3048255,3048436)

#Slovakia
#getLinks(3032576,3032707)

#Slovenia
getLinks(3039484,3039663)

#Serbia
getLinks(3030015,3030254)

#Isreal League 
#getLinks(3033612,3033793)

#Hungary League 
getLinks(3050532,3050729)

#Belarus
getLinksFromFile("Belarus 20")

#Brasil Serie A
#getLinks(,)

#Brasil Serie B
#getLinks(,)

#LigaMx
#Apertura
#getLinks(3040957,3041127)
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
#getLinks(,)

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
#getLinks(3172275,3172580)

#A-League
getLinks(3129271,3129413)

#MLS
#getLinks(3195739,3196180)

#getLinks(,)
