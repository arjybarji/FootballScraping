import requests
from bs4 import BeautifulSoup
import time
import numpy as np
import uuid
import time
from multiprocessing import Pool
import sys, os

teams = open('teams.csv','w',encoding='utf-8')

with open('fixturesv2.csv',encoding='utf-8') as f:
    content = f.readlines()
content = [x.strip() for x in content]

teamsList = []

for c in content:
    split = c.split(",")
    print(split)
    if split[0] not in teamsList:
        teamsList.append(split[0])
        teams.write(split[0] + "\n")
    if split[1] not in teamsList:
        teamsList.append(split[1])
        teams.write(split[1] + "\n")