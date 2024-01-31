#!/usr/bin/env python
# coding: utf-8
# %%

# # Web scraping stat BRK

# %%


import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


# %%


url = "https://leagueoflegends.fandom.com/wiki/Blade_of_the_Ruined_King"
url


# %%


response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")


# ## Bases stats

# %%


brk_stat = html.findAll("div",{"class" : "pi-data-value pi-font"})[:3]
brk_stat


# %%


for idx,stats in enumerate(brk_stat):
    brk_stat[idx] = re.search(r'(\d+)', stats.text).group(1)

# take account of %
brk_stat = list(map(int,brk_stat))
brk_stat[1] /=100
brk_stat[2] /=100
print(brk_stat)


# ## HP % Passive

# %%


#brk_passives = html.findAll("div",{"class" : "pi-data-value pi-font"})[3:5]
brk_passive  = html.find("span",{"style": "white-space:pre; position:relative;", "data-game"  : "lol"})
brk_passive = brk_passive.text
brk_passive = re.search(r'(\d+)', brk_passive).group(1)
brk_passive = float(brk_passive) / 100
brk_passive


# %%


brk_passive_range  = html.find("span",{"style": "white-space:pre; position:relative;", "data-game"  : "lol" , "data-tip" : "Ranged"})
brk_passive_range = brk_passive_range.text
brk_passive_range = re.search(r'(\d+)', brk_passive_range).group(1)
brk_passive_range = float(brk_passive_range) / 100
brk_passive_range


# ## Slow passive

# %%


brk_3autos = html.find("span",{"style" : "position:relative; border-bottom:1px dotted; cursor:help;"})
print(brk_3autos['data-bot_values'])
print(brk_3autos['data-top_values'])


# %%


three_autos_lvl = brk_3autos['data-top_values'].split(";")
print(three_autos_lvl)
three_autos_dmg = brk_3autos['data-bot_values'].split(";")
print(three_autos_dmg)

three_autos_dict = {key: value for key, value in zip(three_autos_lvl, three_autos_dmg)}
print(three_autos_dict)


# ## Item creation

# %%

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy


# %%


brk_dict = {"ad" : brk_stat[0], "as" : brk_stat[1], "lifesteal" : brk_stat[2]}
brk_dict['passive'] = brk_passive
brk_dict['three_autos'] = three_autos_dict
brk_dict_range = copy.deepcopy(brk_dict)
brk_dict_range['passive'] = brk_passive_range


# %%


BRK_melee = Item("brk", brk_dict)
BRK_range = Item("brk", brk_dict_range)


# %%


print(BRK_melee)
print(BRK_range)


# %%
def createBRK(melee : bool = True):
    if melee:
        return Item("brk", brk_dict)
    else:
        return Item("brk", brk_dict_range)
