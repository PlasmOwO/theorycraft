# # Web scraping for Terminus

# *Be careful, this is considered as an Armor pen AND magic pen item*  
# *You cannot have multiple pen items*

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Terminus"
url

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

# ## Base stats

# +
terminus_stat = html.findAll("div",{"class" : "pi-data-value pi-font"})[:2]
for idx,stats in enumerate(terminus_stat):
    terminus_stat[idx] = re.search(r'(\d+)', stats.text).group(1)

# take account of %
terminus_stat = list(map(int,terminus_stat))
terminus_stat[1] /=100
terminus_stat
# -

# ## On hit effect

terminus_onhit = html.find("div",{"class" : "pi-item pi-data pi-item-spacing pi-border-color", "data-source":"pass"})
terminus_onhit = int(re.findall(r'\b\d+\b|\b\d+\.\d+\b', terminus_onhit.text)[0])
terminus_onhit

# ## Armor bonus

# +
terminus_bonus_resi = html.findAll("span",{"style" : "position:relative; border-bottom:1px dotted; cursor:help;"})[1]
terminus_bonus_resi_index = range(1,19)
terminus_bonus_resi_val = terminus_bonus_resi['data-bot_values']

terminus_bonus_resi_val = terminus_bonus_resi_val.split(";")

terminus_bonus_resi_val = [float(x) for x in terminus_bonus_resi_val]
terminus_resi = {key : value for key, value in zip(terminus_bonus_resi_index,terminus_bonus_resi_val)}
terminus_resi
# -

# ## Pen bonus

"""armor_pen_span = html.find_all('span', style="color:yellow; white-space:normal")[-1]

# Accéder au texte situé juste avant cette balise
terminus_pen = armor_pen_span.find_previous(text=True)
terminus_pen = (int((re.findall(r'\b\d+\b|\b\d+\.\d+\b', terminus_pen)[0]))/100)*3
terminus_pen"""
terminus_pen = 0.20

# ## Item creation

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy

terminus_dict = {"ad" : terminus_stat[0], "as" : terminus_stat[1]}
terminus_dict['on-hit'] = terminus_onhit
terminus_dict['armor'] = terminus_resi
terminus_dict['magic_res'] = terminus_resi
terminus_dict['armor_pen'] = terminus_pen
terminus_dict['mr_pen'] = terminus_pen

Terminus = Item("terminus", terminus_dict)


def createTerminus():
    return Item("terminus", terminus_dict)


