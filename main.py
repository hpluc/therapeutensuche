import requests
from bs4 import BeautifulSoup

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

print(GetTherapeutenJason(64293,10))