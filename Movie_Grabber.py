#!/usr/bin/python

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

filename = "movies.csv"
f = open(filename, "w")
headers = "Title, Director, Category, Hearts, Link\n"
f.write(headers)

my_url = 'https://2019.tiffr.com/shows'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

film_data = page_soup.find("ul",{"class":"categories-list"})
film_links = film_data.find_all('a')

for link in film_links:
#    print("2019.tiffr.com/" + link.get('href'))
    film_url = "https://2019.tiffr.com" + link.get('href')
    uClient = uReq(film_url)
    film_page_html = uClient.read()
    uClient.close()
    film_soup = soup(film_page_html, "html.parser")

    film_masthead = film_soup.find("div",{"class":"film__masthead"})
    page_heart = film_soup.find("div",{"id":"film-page-heart"})

    if film_masthead.h2 == None:

        film_title = film_masthead.h1.get_text()
        film_category = film_masthead.a.get_text()

        heart_count = page_heart["data-count"]

        print("Title: " + film_title)
        print("Category: " + film_category)
        print("Hearts: " + heart_count)
        print("Link: " + film_url)

        f.write(film_title.replace(",", "|") + "," + "N/A" + "," + film_category + "," + heart_count + "," + film_url + "\n")
#    elif page_heart == None:
#
#        film_title = film_masthead.h1.get_text()
#        film_director = film_masthead.h2.get_text()
#        film_category = film_masthead.a.get_text()

#        f.write(film_title.replace(",", "|") + "," + film_director.replace(",", "|") + "," + film_category + "," + "N/A" + "\n")

    else:
        film_title = film_masthead.h1.get_text()
        film_director = film_masthead.h2.get_text()
        film_category = film_masthead.a.get_text()

        heart_count = page_heart["data-count"]

    #    print(page_heart)
        print("Title: " + film_title)
        print("Director: " + film_director)
        print("Category: " + film_category)
        print("Hearts: " + heart_count)
        print("Link: " + film_url)

        f.write(film_title.replace(",", "|") + "," + film_director.replace(",", "|") + "," + film_category + "," + heart_count + "," + film_url + "\n")
#    f.write(film_title + "," + film_director + "," + film_category + "\n")
f.close()
#    film_card = film_soup.find("div",{"class":"film-card__metadata"})
#
#    f.write(str(film_card.prettify(formatter="html")))
#f.close()
    #print(str(film_soup.prettify(formatter="html")))
    #film_card = film_soup.find("div",{"class":"film-card__metadata"})



    #print(film_title)
    #film_title = film_masthead.h1.get_text()


#print(film_list.find_all('a'))
