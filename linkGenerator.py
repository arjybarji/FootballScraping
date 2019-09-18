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
#Eredivisie
getLinks(3032053,3032358)
#English Lower Leagues
getLinks(3035129,3036784)
#La Liga
getLinks(3058810,3059189)
#Ligue1
getLinks(3030547,3030926)
#Bundesliga
getLinks(3047020,3047325)
#Portugal League
getLinks(3064644,3064949)
#Eerste Divisie
getLinks(3031673,3032052)
#2. Bundes
getLinks(3047327,3047632)
# Serie B
getLinks(3122543,3122922)
#Ligue 2
getLinks(3031016,3031395)
#Segunda Division
getLinks(3059913,3060374)
# Segunda Liga
getLinks(3065081,3065386)
#Scotland Premier
getLinks(3038361,3038558)
#Scotland Championship
getLinks(3038559,3038738)
#A-League
getLinks(3129271,3129413)
#Turkey
getLinks(3081777,3082082)
#J1 League
getLinks(2972889,2973141)
#Brasil Serie A
getLinks(2988916,2989295)
#China
getLinks(2979871,2980110)
#Denmark
getLinks(3026880,3027061)
#Norway
getLinks(2951376,2951615)
#Russia
getLinks(3027073,3027312)
#Ireland
getLinks(2950168,2950347)
#Austria
getLinks(3034837,3034968)
#Belgium
getLinks(3050137,3050387)
#Czech
getLinks(3036786,3037025)
#Croatia
getLinks(3029812,3029991)
#Poland
getLinks(3025700,3025939)        
#Sweden
getLinks(2947130,2947369)
#Switzerland
getLinks(3037815,3037994)
#Finland
getLinks(2967551,2967682)
#LigaMx
getLinks(3040957,3041127)
#National League
getLinks(3053879,3054430)
#National League North and South
getLinks(3054487,3055410)
#Greece
getLinks(3051869,3052050)
#Romania
getLinks(3048255,3048436)
#Brasil Serie B
getLinks(2987874,2988253)
