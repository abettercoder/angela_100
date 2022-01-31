from bs4 import BeautifulSoup

with open("Day45/bs4/site.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
print(soup.title.string)
