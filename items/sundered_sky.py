# # Web scraping for Sundered Sky

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Sundered_Sky"
url

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

# ## Base stats

# +
sundered = html.findAll("div",{"class" : "pi-data-value pi-font"})[:3]
for idx,stats in enumerate(sundered):
    sundered[idx] = re.search(r'(\d+)', stats.text).group(1)

# take account of %
sundered = list(map(int,sundered))
# -

# ## Auto empowered

# +
heal_span = html.find('span', {"data-tip" : "Heal"})

empowered_auto = heal_span.find_previous(text=True)
empowered_auto =  (int((re.findall(r'\b\d+\b|\b\d+\.\d+\b', empowered_auto)[0]))/100)
# -

empowered_auto

# ## Item creation

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy

sundered_dict = {"ad" : sundered[0], "haste" : sundered[1], "hp" : sundered[2]}
sundered_dict['pass_auto'] = empowered_auto


Sundered_sky = Item("sundered_sky",sundered_dict)


def createSunderedSky():
    return Item("sundered_sky", sundered_dict)
