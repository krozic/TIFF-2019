#!/usr/bin/python

import string
import os
import time
from twilio.rest import Client

account_sid = 'account_sid'
auth_token = 'auth_token'

client = Client(account_sid, auth_token)

import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

movies = [
    "TheLighthouseRyerson",
    "ParasiteRyerson",
    "ColorOutofSpaceRyerson",
    "JojoRabbitPrincess",
    "JokerRoy",
    "KnivesOutElgin",
    "KnivesOutPrincess"
]

upmovies = [
]

while True:
    my_url = 'https://tiff.net/availability-list'
    uClient = urlopen(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = BeautifulSoup(page_html, "html.parser")

    film_data = page_soup.find("div",{"class":"availability-table"})
    data = str(film_data.get_text())
    nonewline = data.replace("\n", " ")
    string_data = nonewline.replace(" ", "")

    for movie in movies:
        if movie in string_data:
            client.messages.create(
                to="+1234567890",
                from_="+1234567890",
                body=movie
            )
            client.messages.create(
                to="+1234567890",
                from_="+1234567890",
                body=movie
            )
            client.messages.create(
                to="+1234567890",
                from_="+1234567890",
                body=movie
            )
            client.messages.create(
                to="+1234567890",
                from_="+1234567890",
                body=movie
            )

            movies.remove(movie)
            upmovies.append(movie)

    for upmovie in upmovies:
        # print(upmovie)
        if str(upmovie in string_data) == "False":
            unavailable = upmovie + "unavailable"
            client.messages.create(
                to="+1234567890",
                from_="+1234567890",
                body=unavailable
            )
            upmovies.remove(upmovie)
            movies.append(upmovie)

    time.sleep(3)
