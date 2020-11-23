import requests
from requests import get
from bs4 import BeautifulSoup
from listy import baseurl
from listy import url
from listy import loca
import pandas as pd
import numpy as np
import requests
from time import sleep
from random import randint

#Dallas Arts Museum
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
results = requests.get(url[0], headers=headers)

soup = BeautifulSoup(results.text, 'lxml')

titles = []
dates = []
locations = []
descriptions = []
urls = []

#Titles & locations
arts_div = soup.find_all('h3')
print('Finding title ' + str(arts_div))
for container in arts_div:
    name = container.text.strip()
    print(name)
    titles.append(name)
    locations.append(loca[0])

#date
arts_div = soup.find_all('span', class_='date-display-range')    
print('Finding dates')
for container in arts_div:
    date = container.text.strip()
    print(date)
    dates.append(date)
    
#description
arts_div = soup.find_all('div', class_='field-item even')
for containter in range(10):
    desc = 'Click the event for more info'
    print(desc)
    descriptions.append(desc)

#URLs
arts_div = soup.find_all('h3', class_='node-title')    
print('Finding URLs')
for container in arts_div:
    for link in container.find_all('a', href=True):
        print(link['href'])
        urls.append(baseurl[0] + link['href'])
 
#Crow Museum
results = requests.get(url[1], headers=headers)

soup = BeautifulSoup(results.text, 'lxml')

#Titles & locations
arts_div = soup.find_all('p', class_='event-title')
print('Finding title ' + str(arts_div))
for container in arts_div:
    print(container.text)
    name = container.text.strip()
    titles.append(name)
    locations.append(loca[1])

#Date
try:
    arts_div = soup.find_all('p', class_='event-date-inline meta')
except:
    arts_div = 'Not Available'        
print('Finding dates')
for container in arts_div:
    print(container.text)
    date = container.text.strip()
    dates.append(date)

#Description
arts_div = soup.find_all('span', class_='excerpt')
for containter in arts_div:
    desc = container.text
    print(desc)
    descriptions.append(desc)

#URLs
arts_div = soup.find_all('p', class_='event-title')    
print('Finding URLs')
for container in arts_div:
    for link in container.find_all('a', href=True):
        print(link['href'])
        urls.append(link['href'])

#Kimbell Art Museum
results = requests.get(url[2], headers=headers)

soup = BeautifulSoup(results.text, 'lxml')

#Titles & locations
arts_div = soup.find_all('h3', class_='h2 exhibition-promo__title')
print('Finding title ' + str(arts_div))
for container in arts_div:
    print(container.text)
    name = container.text.strip()
    titles.append(name)
    locations.append(loca[2])

#Date
try:
    arts_div = soup.find_all('p', class_='exhibition-promo__desc')
except:
    arts_div = 'Not Available'        
print('Finding dates')
for container in arts_div:
    print(container.text)
    date = container.text.strip()
    dates.append(date)
    
#Description
try:
    arts_div = soup.find_all('h4', class_='exhibition-promo__subtitle')
except:
    arts_div = 'Not Available'
for containter in arts_div:
    print(container.text)
    desc = container.text
    descriptions.append(desc)
    
#URL
arts_div = soup.find_all('div', class_='full-width-inner')    
print('Finding URLs')
for container in arts_div:
    for link in container.find_all('a', href=True, class_='field-promo-image'):
        print(link['href'])
        urls.append(baseurl[2] + link['href'])
        
print(len(url))

#Granada Theater
results = requests.get(url[3], headers=headers)

soup = BeautifulSoup(results.text, 'lxml')

#Titles & locations
arts_div = soup.find_all('div', class_='entry-title summary')
print('Finding title ' + str(arts_div))
for container in arts_div:
    print(container.text)
    name = container.text.strip()
    titles.append(name)
    locations.append(loca[3])

#Date
try:
    arts_div = soup.find_all('div', class_='pkdate')
except:
    arts_div = 'Not Available'        
print('Finding dates')
for container in arts_div:
    print(container.text)
    date = container.text.strip()
    dates.append(date)
    
#Description
try:
    arts_div = soup.find_all('div', class_='ecs-excerpt')
except:
    arts_div = 'Not Available'
for containter in arts_div:
    print(container.text)
    desc = container.text
    descriptions.append(desc)
    
#URL
arts_div = soup.find_all('div', class_='entry-title summary')    
print('Finding URLs')
for container in arts_div:
    for link in container.find_all('a', href=True, class_='field-promo-image'):
        print(link['href'])
        urls.append(link['href'])

#Create List
elist = {
    'Events': titles,
    'Dates' : dates,
    'Locations' : locations,
    'Descriptions' : descriptions,
    'URLS' : urls
}

#Create Dataframe
artevents = pd.DataFrame(elist)

#dataframe
print(artevents)

#datatypes of columns
print(artevents.dtypes)

#where is missing data and how much data is missing 
print(artevents.isnull().sum())

#move all scraped data to a CSV file
artevents.to_csv('arteventstester.csv')