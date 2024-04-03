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

# # Web scraping stats : Black cleaver

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Black_Cleaver"
url

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

# ## Bases stats

bc_stats = html.findAll("div",{"class" : "pi-data-value pi-font"})[:3]
bc_stats

# +
for idx,stats in enumerate(bc_stats):
    bc_stats[idx] = re.search(r'(\d+)', stats.text).group(1)

# take account of %
bc_stats = list(map(int,bc_stats))
# -

# ## Armor Shred

# Armor shred
bc_passiv = html.findAll("span", {"style" : "color:yellow; white-space:normal"})
bc_passiv = bc_passiv[1].text
bc_passiv = re.search(r'(\d+)', bc_passiv).group(1)
bc_passiv = float(bc_passiv) / 100
bc_passiv

# Armor Shred one stack
bc_passiv_one_stack = html.findAll("span", {"style" : "color:yellow; white-space:normal"})
bc_passiv_one_stack = bc_passiv_one_stack[0].text
bc_passiv_one_stack = re.search(r'(\d+)', bc_passiv_one_stack).group(1)
bc_passiv_one_stack = float(bc_passiv_one_stack) / 100
bc_passiv_one_stack

# ## Item Creation

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy

bc_dict = {"ad" : bc_stats[0], "haste" : bc_stats[1], "hp" : bc_stats[2],"BC_one_stack" : bc_passiv_one_stack, "BC_armor_shred" : bc_passiv}
Black_cleaver = Item("black_cleaver", bc_dict)


def createBC():
    return Item("black cleaver",bc_dict)
