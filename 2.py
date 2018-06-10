import requests
from bs4 import BeautifulSoup

iiii="abstr"

for i in range(0,3):
    wordlist=iiii
    url=("https://www.vocabulary.com/dictionary/"+(iiii))
    list = requests.get(url).text
    soup = BeautifulSoup(list, "html.parser")
    qqq = soup.findAll("div", {"class": "autocomplete"})
    qq = soup.find('span', {'class': 'word'})
    ww = qq.string
    print(ww)
    iiii=ww[:2]
    print(iiii)