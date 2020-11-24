import requests
from requests import get
from bs4 import BeautifulSoup
from A1PCListy_David_Ninh import baseurl
from A1PCListy_David_Ninh import url
from A1PCListy_David_Ninh import loca
import pandas as pd
import requests
import datetime
from time import sleep
from random import randint

thisyear = datetime.date.today()

#Dallas Arts Museum
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
results = requests.get(url[0], headers=headers)

soup = BeautifulSoup(results.text, 'lxml')

titles = []
dates = []
locations = []
descriptions = []
urls = []
eventlinks = []

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
arts_div = []
arts_div = soup.find_all('div', class_='field-items')
print(arts_div)
x = 0
for container in arts_div:
    desc = container.text
    print(desc)
    if x == 2:
        #descriptions.append('Not Available')
        print('Not Available')
    else:
        descriptions.append(desc)
    x = x + 1
if arts_div == []:   
    for x in range(10):
        descriptions.append('Not Available')
        print('Not Available')

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
arts_div = []
print('Finding descriptions')
arts_div = soup.find_all('span', class_='excerpt')
for container in arts_div:
    print(container.text)
    desc = container.text
    descriptions.append(desc)
if arts_div == []:   
    for x in range(5):
        descriptions.append('Not Available')
        print('Not Available')

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
print('Finding descriptions')
arts_div = soup.find_all('h4', class_='exhibition-promo__subtitle')
for container in arts_div:
    desc = container.text
    descriptions.append(desc)
if arts_div == []:   
    for x in range(3):
        descriptions.append('Not Available')
        print('Not Available')
    
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
    dates.append(date + ' ' + str(thisyear.year))
    
#Description
print('Finding descriptions')
arts_div = soup.find_all('div', class_='ecs-excerpt')
for container in arts_div:
    desc = container.text
    descriptions.append(desc)
if arts_div == []:   
    for x in range(50):
        descriptions.append('Not Available')
        print('Not Available')
    
#URL
arts_div = soup.find_all('div', class_='entry-title summary') 
print('Finding URLs')
for container in arts_div:
    for link in container.find_all('a'):
        print(link['href'])
        urls.append(link['href'])

#Eismann Center
r = requests.get(url[4])
soup = BeautifulSoup(r.content, 'lxml')
eventlist = soup.find_all('h2', class_='title')

#URLS FOR LIST AND CSV
for item in eventlist:
    for link in item.find_all('a', href=True):
        eventlinks.append(baseurl[4] + link['href'])
        urls.append(baseurl[4] + link['href'])
        print(baseurl[4] + link['href'])

#Titles & locations
arts_div = soup.find_all('h2', class_='title')
print('Finding title ' + str(arts_div))
for container in arts_div:
    print(container.text)
    name = container.text.strip()
    titles.append(name)
    locations.append(loca[4])
        
#Date
try:
    arts_div = soup.find_all('div', class_='link')
except:
    arts_div = 'Not Available'        
print('Finding dates')
badchars = 'Streaming available'
for container in arts_div:
    print(container.text)
    date = container.text.strip()
    date = date.replace(badchars, '')
    print(date)
    dates.append(date)

#Description    
x = 1
for link in eventlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')

    try:
        desc = soup.find('div', class_='tess-content').text.strip()
    except:
        desc = 'dne'
    
    perc = (x / len(eventlinks)) * 100
    print('Saving: ' + str(round(perc)) + '%')
    descriptions.append(desc)
    x = x + 1

    
    
#Dallas Symphony
r = requests.get(url[5])
soup = BeautifulSoup(r.content, 'lxml')
eventlist = soup.find_all('h1', class_='title')

#URLS FOR LIST AND CSV
for item in eventlist:
    for link in item.find_all('a', href=True):
        eventlinks.append(baseurl[5] + link['href'])
        urls.append(baseurl[5] + link['href'])
        print(baseurl[5] + link['href'])

#Titles & locations
arts_div = soup.find_all('h1', class_='title')
print('Finding title ' + str(arts_div))
for container in arts_div:
    print(container.text)
    name = container.text.strip()
    titles.append(name)
    locations.append(loca[5])
        

#Description / Date    
x = 1
for link in eventlinks:
    r = requests.get(link, headers=headers)
    soup = BeautifulSoup(r.content, 'lxml')
    
    try:
        date = soup.find('p', class_='big prod-detail__date').text.strip()
    except:
        date = 'Not Available'    
    try:
        desc = soup.find('div', class_='prod-detail__program_highlights').text.strip()
    except:
        desc = 'dne'
    
    perc = (x / len(eventlinks)) * 100
    print('Saving: ' + str(round(perc)) + '%')
    descriptions.append(desc)
    dates.append(date)
    print(desc)
    print(date)
    x = x + 1

    
    
         
#Create List
elist = {
    'Events': titles,
    'Dates' : dates,
    'Locations' : locations,
    'Descriptions' : descriptions,
    'URLS' : urls
}
print(elist)
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

print('Saving complete. Please refer to artseventstester.csv')