import pandas as pd
stats = pd.read_csv('StatsV2.csv')
stats.columns = ['homeTeam','awayTeam','gameWeek','homeGoals','awayGoals','matchGoals','btts','firstHalfHomeGoals','firstHalfHomeConc','firstHalfAwayGoals','firstHalfAwayConc', 
    'firstHalfTotalGoals','secondHalfHomeGoals','secondHalfHomeConc','secondHalfAwayGoals','secondHalfAwayConc','secondHalfTotalGoals','homeTeamCards','awayTeamCards','matchCards', 
    'homeCorners','awayCorners','homeCornersConc','awayCornersConc','matchCorners','league','gameID']
print(stats.head())
fixtures = pd.read_csv('fixturesv2.csv')
fixtures.columns = ['homeTeam', 'awayTeam','gameWeek','date','league','id']
print(fixtures.head())
print(fixtures['awayTeam'].value_counts())
print(fixtures['homeTeam'].value_counts())
print()