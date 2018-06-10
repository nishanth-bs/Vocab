import requests

from bs4 import BeautifulSoup

def word():
    qq = soup.find('span', {'class': 'word'})
    ww = qq.string
    print(ww)

def vocab():
    url="https://www.vocabulary.com/dictionary/abst"

    list = requests.get(url).text
    soup=BeautifulSoup(list , "html.parser")
    qqq=soup.findAll("div",{"class" : "autocomplete"})
    qq=soup.find('span', {'class' : 'word'})
    ww=qq.string
    print(ww)
    '''for item in qqq:
        if "word" :
            print (item.attr)'''
    '''inputTag = soup.find(attrs={"name": "stainfo"})
    output = inputTag['value']'''
   # qq=qqq['word']
   # print(qqq)
   # eee=soup.findAll("div",{"class":"centeredContent"})
    fff=soup.findAll("p", {"class":"short"})
    print(fff)

    ggg=soup.findAll("p", {"class": "long"})
    print(ggg)
vocab()


    #class section blurb
    #and long

    #class didyoumean ((skip