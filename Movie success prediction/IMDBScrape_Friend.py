from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

url = 'https://www.imdb.com/list/ls021545925/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

first_names = []
first_years = []
first_genres = []
runtime = []
first_rates = []
first_gros = []
first_casts = []
infor = []
movie_containers = soup.find_all('div', class_ = 'lister-item mode-detail')
for first_movie in movie_containers:
    first_name = first_movie.h3.a.text
    first_names.append(first_name)

    first_year = first_movie.h3.find('span', class_ = 'lister-item-year text-muted unbold').text
    first_years.append(first_year)
    
    first_genre = first_movie.p.find('span', class_='genre').text
    first_genres.append(first_genre)

    first_rate = first_movie.find('div', class_='ipl-rating-star small')

    first_rate = first_rate.find('span', class_='ipl-rating-star__rating').text
    first_rates.append(first_rate)

    first_gross = first_movie.find('div', class_='list-description').text
    first_gros.append(first_gross)

    #I am not able to scrape the cast information ........try........this one  

test = pd.DataFrame({'first_year' : first_years,
                     'first_name' : first_names,
                     'first_genre' : first_genres,
                     'first_rates' : first_rates,
                     'first_gros' : first_gros})

print(test.info())
print(test)

"""
url = 'https://www.imdb.com/list/ls021545925/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

overall = soup.select('div.lister-item-content')

imdb = []

for index in range(0, len(overall)):
    new_details = str(overall[index])
    clean_details = BeautifulSoup(new_details, "lxml").get_text()
    data = {"detail": clean_details}
    imdb.append(data)
for item in imdb:
    print(item['detail'])

 first_score = first_movie.find('div', class_='inline-block ratings-metascore')
    first_score = first_score.find('span', class_= 'metascore  favorable').text
    metascores.append(int(first_score))
    
"""
