import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.wiseoldsayings.com/addiction-quotes//")
soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.select(".quote")

for quote in quotes:
    print(quote.getText())
