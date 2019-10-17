

with open('Statsv2.csv',encoding='utf-8') as f:
    content = f.readlines()
content = [x.strip() for x in content]

newStats = open("Statsv21.csv","w",encoding='utf-8')

for c in content:
    a = c.split(",")
    newStats.write(a[0] + "," + a[1] + "," +a[2] + "," +a[3] + "," +a[4] + "," +a[5] + "," +a[6] + "," +a[7] + "," +a[8] + "," +a[9] + "," +a[10] + "," +a[11] + "," +a[12] + "," +a[13] + "," +a[14] + "," +a[15] + "," +a[16] + "," +a[-2] + "," +a[-1] + "\n")