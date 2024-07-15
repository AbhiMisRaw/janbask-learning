import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

product_name = input()
query = "https://www.amazon.in/s?k=" + product_name


fhand = urllib.request.urlopen(query)

soup = BeautifulSoup(fhand, "html.parser")

# tags = soup("div")
tags = soup.select("div > h2")

for tag in tags:
    print(tag.prettify())
