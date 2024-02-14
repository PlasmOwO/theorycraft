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

# # Web scraping stats Kraken slayer

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Kraken_Slayer"
url

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

# ## Bases stats

kraken_stats = html.findAll("div",{"class" : "pi-data-value pi-font"})[:3]
kraken_stats

# +
for idx,stats in enumerate(kraken_stats):
    kraken_stats[idx] = re.search(r'(\d+)', stats.text).group(1)

# take account of %
kraken_stats = list(map(int,kraken_stats))
kraken_stats[1] /=100
kraken_stats[2] /=100
print(kraken_stats)
# -

# ## On-hit proc  
# *Be careful of 50% multiplicator (up to 100%) on the same target*  
# <span style="color:blue"> TODO</span>

bring_it_down = html.find("span", {"style" : "position:relative; border-bottom:1px dotted; cursor:help;"})
bring_it_down_index = bring_it_down['data-top_values']
bring_it_down = bring_it_down['data-bot_values']
print(bring_it_down_index)
print(bring_it_down)

# +
bring_it_down_index = bring_it_down_index.split(";")
bring_it_down = bring_it_down.split(";")

bring_passive = {key : value for key, value in zip(bring_it_down_index,bring_it_down)}
print(bring_passive)
# -

# ## Item Creation

# +

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy
# -

kraken_dict = {"ad" : kraken_stats[0], "as" : kraken_stats[1], "crit" : kraken_stats[2]}
kraken_dict['three_autos'] = bring_passive


Kraken = Item("kraken", kraken_dict)

print(Kraken)
