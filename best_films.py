from bs4 import BeautifulSoup
import requests
import lxml

response = requests.get('https://www.theguardian.com/film/2019/sep/13/100-best-films-movies-of-the-21st-century')
soup = BeautifulSoup(response.text, 'lxml')
movies = soup.find_all(name='h2')
movie_list = []
number_list = 0

for movie in movies:
    date = movie.getText().split()[-1]
    if len(movie.getText()) > 3 and 'comments ' not in movie.getText():
        movie_list.append(movie.getText())
    elif len(movie.getText()) <= 3:
        number_list += 1


movie_list.reverse()
counter = 1
for movie in movie_list:
    print(f"{counter}.{movie}")
    counter += 1
