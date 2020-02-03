import pandas as pd

formBets = pd.read_csv('Book1.csv',header = None)
bets = pd.read_csv('Pred.csv',header = None)
print(bets.head())
print(formBets.head())
merged = pd.merge(bets, formBets, how='inner')
#print(.sort_values(0))
merged.to_csv('combinedBetsDone.csv',index=False,header=False)