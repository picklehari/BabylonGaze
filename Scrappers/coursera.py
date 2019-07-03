import requests
import urllib.request
from bs4 import BeautifulSoup

def return_url(search_term,language="English"):
    #Example URL https://www.coursera.org/courses?query=web%20development&indices[prod_all_products][refinementList][language][0]=English
    head_url = "https://www.coursera.org/courses?query="
    search_term = search_term.lower()
    tail = "&indices[prod_all_products][refinementList][language][0]="
    return head_url + search_term + tail + language

web = return_url("web development")
response = requests.get(web)
soup = BeautifulSoup(response.text, "html.parser")
list = soup.findAll('li',class_="ais-InfiniteHits-item")


