import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession
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

def get_all_forms(url):
    """Returns all form tags found on a web page's `url` """
    # GET request
    res = session.get(url)
    # for javascript driven website
    # res.html.render()
    soup = BeautifulSoup(res.html.html, "html.parser")
    return soup.find_all("form")

def get_form_details(form):
    """Returns the HTML details of a form,
    including action, method and list of form controls (inputs, etc)"""
    details = {}
    # get the form action (requested URL)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, DELETE, etc)
    # if not specified, GET is the default in HTML
    method = form.attrs.get("method", "get").lower()
    # get all form inputs
    inputs = []
    for input_tag in form.find_all("input"):
        # get type of input form control
        input_type = input_tag.attrs.get("type", "text")
        # get name attribute
        input_name = input_tag.attrs.get("name")
        # get the default value of that input tag
        input_value =input_tag.attrs.get("value", "")
        # add everything to that list
        inputs.append({"type": input_type, "name": input_name, "value": input_value})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details



print(GetTherapeutenJason(64293,10))

# initialize an HTTP session
session = HTMLSession()
res = session.get("https://arztsuchehessen.de/arztsuche/arztsuche.php?page=erweiterteSuche&switch=umkreissuche")
res = session.get("https://arztsuchehessen.de/arztsuche/arztsuche.php?page=suche&fachrichtung=44&haus_facharzt=egal&fachrichtung_psycho=--alle--&plz=64283&ort=Darmstadt&entfernung=10&action%5BSucheStarten%5D=&name=--alle--&vorname=--alle--&geschlecht=egal&status=--alle--&genehmigung=--alle--&zusatzbezeichnung=--alle--&testungaufSARSCoV2=--alle--&fremdsprache=--alle--&sz_von_sel=&sz_bis_sel=")
soup = BeautifulSoup(res.content, "html.parser")
#print(soup.text)
table = soup.find('table', {"class": "ergebnisliste"})  # isolate the table
print(table.getText)
#td_list = []  # initialize a list to store the td's we want
#for tr in table.find_all('tr bgcolor="#fbfbfb"'):  # loop through each tr in the table
#    td_list.append(tr.find_all('td')[0])  # append the 2nd td to the td_list
#print(td_list)