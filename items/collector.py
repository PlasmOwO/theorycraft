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

# The Collector 

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/The_Collector"
url

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

# Base stat 

collector_stat = html.findAll("div",{"class" : "pi-data-value pi-font"})[:3]
collector_stat

# +
for idx,stats in enumerate(collector_stat):
    collector_stat[idx] = re.search(r'(\d+)', stats.text).group(1)

collector_stat = list(map(int,collector_stat))
collector_stat[2] /=100
collector_stat
# -

# Item creation

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_item import Item
else :
    from class_item import Item
import copy

collector_dict = {"ad" : collector_stat[0], "as" : collector_stat[1], "lifesteal" : collector_stat[2]}
COLLECTOR_melee = Item("The Collector", collector_dict)
print(COLLECTOR_melee)
