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

# # Web scraping stat Trinity Force

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Trinity_Force"
url

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

# ## Bases stats

# +
triforce_stat = html.findAll("div",{"class" : "pi-data-value pi-font"})[:4]
print(triforce_stat)

for idx,stats in enumerate(triforce_stat):
    triforce_stat[idx] = re.search(r'(\d+)', stats.text).group(1)

# take account of %
triforce_stat = list(map(int,triforce_stat))

triforce_stat[2] /=100
# -

# ## Passive dmg increase

one_stack = html.find("span", {"style" : "color:orange; white-space:normal"})
one_stack = float(re.search(r'(\d+)', one_stack.text).group(1)) / 100


all_stacks = html.findAll("span", {"style" : "color:orange; white-space:normal"})[1]
all_stacks = float(re.search(r'(\d+)', all_stacks.text).group(1)) / 100


# ## Spellblade

spellblade = html.findAll("span", {"style" : "color:orange; white-space:normal"})[2]
spellblade = float(re.search(r'(\d+)', spellblade.text).group(1)) /100
#bug missing

# ## Item Creation

# +

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy

# +
triforce_dict = {"ad" : triforce_stat[0], "haste" : triforce_stat[1],"as" : triforce_stat[2], "hp" : triforce_stat[3]}
triforce_dict['spellblade'] = one_stack

Triforce = Item('triforce', triforce_dict)

# -

def createTriforce():
    return Item("triforce", triforce_dict)
