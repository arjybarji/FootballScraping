links = []
file = open('links.txt','w')
#file = open('AllLinks.txt','w')

def getLinks(start,end):
    for i in range(start,end+1):
        leagueUrl = 'https://us.soccerway.com/matches/2018/08/10/england/premier-league/manchester-united-fc/leicester-city-fc/'
        file.write( leagueUrl +str(i)+'/' + "\n")
for j in range(0,36):
    if(j == 0):
        #Premier League
        getLinks(3029073,3029452)
    elif(j == 1):
        #Serie A
        getLinks(3111700,3112079)
    elif(j == 2):
        #Eredivisie
        getLinks(3032053,3032358)
    elif(j == 3):
        #English Lower Leagues
        getLinks(3035129,3036784)
    elif (j==4):
        #La Liga
        getLinks(3058810,3059189)
    elif (j==5):
        #Ligue1
        getLinks(3030547,3030926)
    elif (j==6):
        #Bundesliga
        getLinks(3047020,3047325)
    elif (j==7):
        #Portugal League
        getLinks(3064644,3064949)
    elif (j==8):
        #Eerste Divisie
        getLinks(3031673,3032052)
    elif (j==9):
        #2. Bundes
        getLinks(3047327,3047632)
    elif (j==10):
        # Serie B
        getLinks(3122543,3122922)
    elif (j==11):
        #Ligue 2
        getLinks(3031016,3031395)
    elif (j==12):
        #Segunda Division
        getLinks(3059913,3060374)
    elif (j==13):
        # Segunda Liga
        getLinks(3065081,3065386)
    elif (j==14):
        #Scotland Premier
        getLinks(3038361,3038558)
    elif (j==15):
        #Scotland Championship
        getLinks(3038559,3038738)
    elif (j==16):
        #A-League
        getLinks(3129271,3129413)
    elif (j==17):
        #Turkey
        getLinks(3081777,3082082)
    elif (j==18):
        #J1 League
        getLinks(2972889,2973141)
    elif (j==19):
        #Brasil Serie A
        getLinks(2988916,2989295)
    elif (j==20):
        #China
        getLinks(2979871,2980110)
    elif (j==21):
        #Denmark
        getLinks(3026880,3027061)
    elif (j==22):
        #Norway
        getLinks(2951376,2951615)
    elif (j==23):
        #Russia
        getLinks(3027073,3027312)
    elif (j==24):
        #Ireland
        getLinks(2950168,2950347)
    elif (j==25):
        #Austria
        getLinks(3034837,3034968)
    elif (j==26):
        #Belgium
        getLinks(3050137,3050387)
    elif (j==27):
        #Czech
        getLinks(3036786,3037025)
    elif (j==28):
        #Croatia
        getLinks(3029812,3029991)
    elif (j==29):
        #Poland
        getLinks(3025700,3025939)        
    elif (j==30):
        #Sweden
        getLinks(2947130,2947369)
    elif (j==31):
        #Switzerland
        getLinks(3037815,3037994)
    elif (j==32):
        #Finland
        getLinks(2967551,2967682)
    elif (j==33):
        #LigaMx
        getLinks(3040957,3041127)
    elif (j==34):
        #National League
        getLinks(3053879,3054430)
    elif (j==35):
        #National League North and South
        getLinks(3054487,3055410)
        