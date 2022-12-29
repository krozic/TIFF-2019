#!/usr/bin/python

import requests
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup
from datetime import datetime
import pandas as pd
pd.set_option('display.max_columns', None)

year = '2022'
my_url = f'https://{year}.tiffr.com/shows'
shows_json = f'https://{year}.tiffr.com/api/{year}/shows.json'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
r = requests.get(shows_json, headers=headers)
data = r.json()

df = pd.DataFrame({
    'Title': [],
    'Director': [],
    'Category': [],
    'Hearts': [],
    'Link': []
})
for movie in data:
    film_url = film_url = f'https://{year}.tiffr.com/shows/' + movie['slug']
    req = Request(film_url, headers=headers)
    uClient = urlopen(req)
    film_page_html = uClient.read()
    uClient.close()
    film_soup = soup(film_page_html, 'html.parser')
    film_masthead = film_soup.find('div', {'class': 'film__masthead'})

    if film_masthead.h2 == None:
        film_director = ''
    else:
        film_director = film_masthead.h2.get_text()
    film_title = film_masthead.h1.get_text()
    film_category = film_masthead.a.get_text()
    heart_count = film_soup.find('div', {'class': 'heart-counter'}).get_text()

    df.loc[len(df)] = [film_title, film_director, film_category, heart_count, film_url]
    print(df.loc[len(df)-1])

today_date = str(datetime.today())[:17].replace(":", "")
table_name = f'movies {today_date}.csv'
df.to_csv(f'./tables/{table_name}', index=False)
