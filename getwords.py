import requests
from bs4 import BeautifulSoup

k=0
for i in range(10,16):

    url = ("http://www.majortests.com/gre/wordlist_"+str(i))
    list = requests.get(url).text
    soup = BeautifulSoup(list, "html.parser")
    group = soup.findAll("table",{"class":"wordlist"})
    for i in group:
        word = i.findAll("th")
        for j in word:
            print("\""+j.get_text()+"\",",end=" ")
            k += 1
print (k)