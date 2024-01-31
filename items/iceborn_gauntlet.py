# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Web scraping stats Iceborn Gauntlet

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Iceborn_Gauntlet"
url

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

# ## Bases stats

iceborn_stats = html.findAll("div",{"class" : "pi-data-value pi-font"})[:3]
iceborn_stats

# +
for idx,stats in enumerate(iceborn_stats):
    iceborn_stats[idx] = re.search(r'(\d+)', stats.text).group(1)

# take account of %
iceborn_stats = list(map(int,iceborn_stats))
print(iceborn_stats)
# -

# ## SpellBlade

spellblade = html.findAll("span", {"style" : "color:orange; white-space:normal"})[2]
spellblade = float(re.search(r'(\d+)', spellblade.text).group(1)) /100
print(spellblade)

# ## Item Creation

# %run class_item.ipynb

iceborn_dict = {"haste" : iceborn_stats[0], "armor" : iceborn_stats[1], "hp" : iceborn_stats[2],"spellblade" : spellblade}


Iceborn = Item("iceborn", iceborn_dict)

print(Iceborn)
