import requests
from bs4 import BeautifulSoup
url = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
website_html = response.text
# make a soup object
soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())
all_h3 = soup.find_all(name="h3")
# print(all_h3)
# get all the h3 tags using find_ll()
all_movies = soup.find_all(
    name="h3", class_="listicleItem_listicle-item__title__hW_Kn")
# # if you are finding tag name than you can use name="tag_name"
# print(all_movies.gettext())

movies_title = [movies.getText() for movies in all_movies]
# print(movies_title)
# if you want to print movies list in reverse

movies = movies_title[::-1]

# for i in range(len(all_movies)-1, -1, -1):
#     print(movies_title[i])

with open("movies.txt", "a") as file:
    for movie in movies:
        file.write(f"{movie}\n")
