links = []
file = open('links.txt','w')
#file = open('AllLinks.txt','w')

def getLinks(start,end):
    for i in range(start,end+1):
        leagueUrl = 'https://us.soccerway.com/matches/2018/08/10/england/premier-league/manchester-united-fc/leicester-city-fc/'
        file.write( leagueUrl +str(i)+'/' + "\n")

def getLinksFromFile(fileq):
    with open(fileq) as f:
        content = f.readlines()
    for c in content:
        c.strip()
        file.write( c)

#Premier League
getLinks(3029073,3029452)
#English Lower Leagues
getLinks(3035129,3036784)
#National League
getLinks(3053879,3054430)
#National League North and South
getLinks(3054487,3055410)
#Scotland Premier
getLinks(3038361,3038558)
#Scotland Championship
getLinks(3038559,3038738)
#Scotland League One
getLinks(3038181,3038360)
#Scotland League 2
getLinks(3038739,3038918)
#Ireland
#getLinks(2950168,2950347)
#Wales
getLinks(3042798,3042929)
#Serie A
getLinks(3111700,3112079)
#Serie B
getLinks(3122543,3122922)
#La Liga
getLinks(3058810,3059189)
#Segunda Division
getLinks(3059913,3060374)
#Bundesliga
getLinks(3047020,3047325)
#2. Bundes
getLinks(3047327,3047632)
#3. Bundesliga
getLinks(3053138,3053517)
#Ligue1
getLinks(3030547,3030926)
#Ligue 2
getLinks(3031016,3031395)
#National 1 
getLinks(3073147,3073452)
#Portugal League
getLinks(3064644,3064949)
#Segunda Liga
getLinks(3065081,3065386)
#Eredivisie
getLinks(3032053,3032358)
#Eerste Divisie
getLinks(3031673,3032052)
#Austria
getLinks(3034837,3034968)
#Austria 2
getLinks(3040372,3040611)
#Denmark
getLinks(3026880,3027061)
#Norway
#getLinks(2951376,2951615)
#Sweden
#getLinks(2947130,2947369)
#Finland
#getLinks(2967551,2967682)
#Belgium
getLinks(3050137,3050387)
#Czech
getLinks(3036786,3037025)
#Croatia
getLinks(3029812,3029991)
#Poland
getLinks(3025700,3025939)
#Russia
getLinks(3027073,3027312)       
#Switzerland
getLinks(3037815,3037994)
#Turkey
getLinks(3081777,3082082)
#Greece
getLinks(3051869,3052050)
#Romania
getLinks(3048255,3048436)
#Slovakia
getLinks(3032576,3032707)
#Serbia
getLinks(3030015,3030254)
#Isreal League 
getLinks(3033612,3033793)
#Brasil Serie A
#getLinks(2988916,2989295)
#Brasil Serie B
#getLinks(2987874,2988253)
#LigaMx
#getLinks(3040957,3041127)
#Argentina
getLinks(3070319,3070594)
#China
#getLinks(2979871,2980110)
#J1 League
#getLinks(2972889,2973141)
#getLinks(3002549,3002564)
#getLinks(3131532,3131556)
#J2 League
#getLinks(2972277,2972739)
#A-League
getLinks(3129271,3129413)
#getLinks(,)


