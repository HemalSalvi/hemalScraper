import requests
from bs4 import BeautifulSoup

website = requests.get("https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html")
soup = BeautifulSoup(website.content, "html.parser")

cases = soup.find("div", {"class": "card-body bg-white"})
print(cases.li.contents)