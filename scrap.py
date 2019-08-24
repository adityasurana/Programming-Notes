import urllib.request
import requests
from bs4 import BeautifulSoup as BS
page=requests.get("https://timesofindia.indiatimes.com")
soup = BS(page.content, 'html.parser')
data = soup.find_all("div",{"id":"top-story"})
data2=soup.find(class_="list8").get_text()
print(data2)

