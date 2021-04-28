import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import re
from urllib.parse import urljoin

def GetTherapeutenJason (Postleitzahl, Umkreis):
    try:
        #url2 = "https://arztsuchehessen.de/arztsuche/arztsuche.php?page=suche&fachrichtung=--alle--&haus_facharzt=egal&fachrichtung_psycho=479&plz="+str(Postleitzahl)+"&entfernung="+str(Umkreis)+"&action%5BSucheStarten%5D=&name=--alle--&vorname=--alle--&geschlecht=egal&status=--alle--&genehmigung=--alle--&zusatzbezeichnung=--alle--&testungaufSARSCoV2=--alle--&fremdsprache=--alle--&sz_von_sel=&sz_bis_sel="
        url2="https://arztsuchehessen.de/arztsuche/arztsuche.php?page=ergebnisliste&filter=aktiv&standort=64283%3BDarmstadt%3B%3B49.872356%3B8.650903&action%5BSucheStarten%5D="
        print(url2)
        #diese blöde Url funktioniert noch nicht
        req = requests.get(url2)
        bsObj = BeautifulSoup(req.text, "html.parser")
        table = bsObj.find('table', {"class": "ergebnisliste"})  # isolate the table
        td_list = []  # initialize a list to store the td's we want
        print(bsObj)
        for tr in table.find_all('tr'):  # loop through each tr in the table
            td_list.append(tr.find_all('td')[0])  # append the 2nd td to the td_list
            print(tr.find_all('td')[0])
        url = "https://arztsuchehessen.de/arztsuche/arztsuche.php?page=karteikarte&arztID=48846&status=70342&zulknz=V&adrkey=152328&bstkey=77228"
        req = requests.get(url)
        bsObj = BeautifulSoup(req.text, "html.parser")
        data_all = bsObj.find_all("div",class_ = "Sprechzeit")
        NumConfirmed = data_all[0].text.strip().replace(':', '')
        return {
            'NumConfirmed': NumConfirmed
        }
    except Exception as e: print(e)

def getAerzte():
    url ="https://arztsuchehessen.de/arztsuche/arztsuche.php?page=suche&fachrichtung=--alle--&haus_facharzt=egal&fachrichtung_psycho=479&plz=64293&ort=Darmstadt&entfernung=5&action%5BSucheStarten%5D=&name=--alle--&vorname=--alle--&geschlecht=egal&status=--alle--&genehmigung=--alle--&zusatzbezeichnung=--alle--&testungaufSARSCoV2=--alle--&fremdsprache=--alle--&sz_von_sel=&sz_bis_sel="

# initialize an HTTP session
session = HTMLSession()
res = session.get("https://arztsuchehessen.de/arztsuche/arztsuche.php?page=erweiterteSuche&switch=umkreissuche")
res = session.get("https://arztsuchehessen.de/arztsuche/arztsuche.php?page=suche&fachrichtung=44&haus_facharzt=egal&fachrichtung_psycho=--alle--&plz=64283&ort=Darmstadt&entfernung=10&action%5BSucheStarten%5D=&name=--alle--&vorname=--alle--&geschlecht=egal&status=--alle--&genehmigung=--alle--&zusatzbezeichnung=--alle--&testungaufSARSCoV2=--alle--&fremdsprache=--alle--&sz_von_sel=&sz_bis_sel=")
res= session.get("https://arztsuchehessen.de/arztsuche/arztsuche.php?page=ergebnisliste&rpp=100")
soup = BeautifulSoup(res.content, "html.parser")
table = soup.find('table', {"class": "ergebnisliste"})  # isolate the table
td_list = []  # initialize a list to store the td's we want
links = []
i=int(0)
for td in table.find_all('td'):  # loop through each tr in the table
    i = i + 1
    if i == 1:
        td_list.append(td)
        #print(td)
        link = re.findall('arzt.*[0-9]"',str(td))
        links.append(link[0])
        #print (link)
    if i == 3:
        i=0
for link in links:
    link = link[:-1]
    link = link.replace("amp;","")
    link = "https://arztsuchehessen.de/arztsuche/" + link
    print (link)
    res = session.get(link)
    soup = BeautifulSoup(res.content, "html.parser")
    data_all = soup.find_all("div", class_="Sprechzeit")
    #Sprechzeit = re.findall('Telefonische Erreichbarkeit .* Sprechstunde', str(soup.text))
    print (data_all)