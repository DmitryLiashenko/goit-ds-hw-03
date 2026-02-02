import json
import requests
from bs4 import BeautifulSoup
from connect_to_db import get_client


url = "https://quotes.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
quotes = soup.find_all("div", class_="quote")


myquotes = []
for quote in quotes:
    q = {}
    q["tags"] = [tag.text for tag in quote.find_all("a", class_="tag")]
    q["author"] = quote.find("small", class_="author").text
    q["quote"] = quote.find("span", class_="text").text
    myquotes.append(q)

myauthors = []
list_of_authors = []
for quote in quotes:
    author_link = url + quote.find("a")["href"]
    list_of_authors.append(quote.find("small", class_="author").text)
    if quote.find("small", class_="author").text not in list_of_authors:
        list_of_authors.append(author_link)
        response = requests.get(author_link)
        soup = BeautifulSoup(response.text, "lxml")
        author = soup.find("div", class_="author-details")
        a = {}
        a["fullname"] = author.find("h3", class_="author-title").text
        a["born_date"] = author.find("span", class_="author-born-date").text
        a["born_location"] = author.find("span", class_="author-born-location").text
        a["description"] = author.find("div", class_="author-description").text.strip()
        myauthors.append(a)


with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(myquotes, f, ensure_ascii=False, indent=4)


with open("authors.json", "w", encoding="utf-8") as f:
    json.dump(myauthors, f, ensure_ascii=False, indent=4)
sdfsdfd