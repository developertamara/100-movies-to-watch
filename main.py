import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")
# print(soup.prettify())

top_100_movies = []
movie_names = soup.findAll('h3', class_='title')

file_name = "top_100_movies.txt"
movie_names.reverse()
with open(file_name, "w") as file:
    file.write("Top 100 Movies of All Time \n")
    file.write("---------------------------\n")
    for movie in movie_names:
        titles = movie.getText()
        top_100_movies.append(titles)
        file.write(f"{titles}\n")

print(f"File '{file_name}' has been created successfully.")
print(top_100_movies)
