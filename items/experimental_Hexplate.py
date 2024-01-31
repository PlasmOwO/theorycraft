# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# Experimenal Hexplate

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Experimental_Hexplate"
url

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

# Base Stats

eh_stat_ad = html.find("div",{"class" : "pi-item pi-data pi-item-spacing pi-border-color", "data-source": "ad" })
eh_stat_ad = eh_stat_ad.text
eh_stat_ad = re.search(r'(\d+)', eh_stat_ad).group(1)
eh_stat_ad

eh_stat_as = html.find("div",{"class" : "pi-item pi-data pi-item-spacing pi-border-color", "data-source": "as" })
eh_stat_as = eh_stat_as.text
eh_stat_as = re.search(r'(\d+)', eh_stat_as).group(1)
eh_stat_as = float(eh_stat_as)/100
eh_stat_as

eh_stat_hp = html.find("div",{"class" : "pi-item pi-data pi-item-spacing pi-border-color", "data-source": "hp" })
eh_stat_hp = eh_stat_hp.text
eh_stat_hp = re.search(r'(\d+)', eh_stat_hp).group(1)
eh_stat_hp

# Passive

# Hexcharged

eh_passsive_hexcharged = html.find("div",{"class": "pi-item pi-data pi-item-spacing pi-border-color", "data-source": "pass"})
eh_passsive_hexcharged = eh_passsive_hexcharged.text
eh_passsive_hexcharged = re.search(r'(\d+)', eh_passsive_hexcharged).group(1)
print(eh_passsive_hexcharged)

eh_passive = html.find("span",{"style": "color:orangered; white-space:normal"})
eh_passive = eh_passive.text
eh_passive = re.search(r'(\d+)', eh_passive).group(1)
print(eh_passive)

eh_passive2 = html.find("span",{"style": "color: #F5EE99; white-space:normal"})
eh_passive2 = eh_passive2.text
eh_passive2 = re.search(r'(\d+)', eh_passive2).group(1)
print(eh_passive2)

# Item cration 

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy

eh_dict = {"ad" : eh_stat_ad, "as" : eh_stat_as, "lifesteal" : eh_stat_hp}
eh_dict['passive'] = eh_passsive_hexcharged

EH_melee = Item("Experimenal Hexplate", eh_dict)
print(EH_melee)
