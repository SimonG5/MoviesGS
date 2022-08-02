import json
import requests
from bs4 import BeautifulSoup

movies = []
with open('datasets/movies.dat', 'r', encoding="UTF8")as f:
    movies = f.readlines()


print(movies)
dict = {}

for i in range(1, 1500, 50):
    print(i)
    URL = f"https://www.imdb.com/search/title/?title_type=feature&num_votes=10000,&countries=us&sort=user_rating,desc&start={i}&ref_=adv_nxt"
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    for j in range(1, 51):
        r = soup.select_one(
            f'#main > div > div.lister.list.detail.sub-list > div > div:nth-child({j}) > div.lister-item-content > div > div.inline-block.ratings-imdb-rating > strong')
        i = soup.select_one(
            f'#main > div > div.lister.list.detail.sub-list > div > div:nth-child({j}) > div.lister-item-content > h3 > a')
        for mov in movies:
            format = mov.split("::")
            if format[1].rstrip() == i.text:
                dict[format[0]] = r.text

with open("averageRatings.json", "w") as outfile:
    json.dump(dict, outfile)
