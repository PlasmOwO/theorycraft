import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Titanic_Hydra"
response = requests.get(url)

url

html = BeautifulSoup(response.text, "html.parser")

# +
titanic = html.findAll("div",{"class" : "pi-data-value pi-font"})[:2]
for idx,stats in enumerate(titanic):
    titanic[idx] = re.search(r'(\d+)', stats.text).group(1)

# take account of %
titanic = list(map(int,titanic))
# -

titanic

# Titanic Passive

# +
cleave = html.findAll("div",{"class" : "pi-item pi-data pi-item-spacing pi-border-color", "data-source" : "pass"})
for element in cleave :
    titanic_cleave_passive = element.find("span",{"class" : "glossary", "data-tip": "Melee"}).text
    
titanic_cleave_passive = float(re.sub(r'[^0-9.]', '', titanic_cleave_passive))/100
titanic_cleave_passive = str(titanic_cleave_passive) + " * HP"

titanic_cleave_passive

# -

# Titanic Active

# +
active_cleave = html.findAll("div",{"class" : "pi-item pi-data pi-item-spacing pi-border-color", "data-source" : "act"})
for element in active_cleave :
    titanic_cleave_active = element.find("span",{"class" : "glossary", "data-tip": "Melee"}).text
    
titanic_cleave_active = float(re.sub(r'[^0-9.]', '', titanic_cleave_active))/100
#add ratio
titanic_cleave_active = str(titanic_cleave_active) + " * HP"
titanic_cleave_active

# -

# ## Item creation

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy

titanic_dict = {"ad": titanic[0], "hp" : titanic[1], "titanic_passive_cleave" : titanic_cleave_passive , "titanic_active_cleave" : titanic_cleave_active}

Titanic = Item("titanic_hydra",titanic_dict)
print(Titanic)


def createTitanic():
    return Item("titanic_hydra",titanic_dict)


