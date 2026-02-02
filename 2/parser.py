import time
import json
import requests
from bs4 import BeautifulSoup
from connect_to_db import get_client


base_url = "https://quotes.toscrape.com/"
myquotes = []
myauthors = []
list_of_authors = []


url = "https://quotes.toscrape.com/"


while True:
    try:
        response = requests.get(url)
        time.sleep(0.5)
        parent_soup = BeautifulSoup(response.text, "lxml")
        quotes = parent_soup.find_all("div", class_="quote")
        for quote in quotes:
            q = {}
            q["tags"] = [tag.text for tag in quote.find_all("a", class_="tag")]
            q["author"] = quote.find("small", class_="author").text
            q["quote"] = quote.find("span", class_="text").text
            myquotes.append(q)

        for quote in quotes:
            author_link = base_url + quote.find("a")["href"]
            if author_link not in list_of_authors:
                list_of_authors.append(author_link)
                response = requests.get(author_link)
                time.sleep(0.5)
                author_soup = BeautifulSoup(response.text, "lxml")
                author = author_soup.find("div", class_="author-details")
                a = {}
                a["fullname"] = author.find("h3", class_="author-title").text
                a["born_date"] = author.find("span", class_="author-born-date").text
                a["born_location"] = author.find("span", class_="author-born-location").text
                a["description"] = author.find("div", class_="author-description").text.strip()
                myauthors.append(a)
        next_page = parent_soup.find("li", class_="next")
        if next_page:
            href = next_page.a["href"]
            url = base_url + href
        else:
            break
    except Exception as e:
        print(f"Something wrong {e}")
        break


with open("quotes.json", "w", encoding="utf-8") as f:
    json.dump(myquotes, f, ensure_ascii=False, indent=4)


with open("authors.json", "w", encoding="utf-8") as f:
    json.dump(myauthors, f, ensure_ascii=False, indent=4)
