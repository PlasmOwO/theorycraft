# %% [markdown]
# # Global Vars that will be used during the automation

# %% [markdown]
# | Global vars |
# |----------
# | BONUS_AD ||
# | AD       |
# | BASE_AD |
# | AP       |
# | HP       |
# | BONUS_HP |
# |TARGET_MISSING_HP|
# |TARGET_CURRENT_HP |
# |CRIT_CHANCE|
# |AS |
# |IE|

# %% [markdown]
# current and mising will be the same i guess

# %%
# utiliser sys.path

# Script : Faire une fonction qui **return** un objet Item

import pandas as pd
import numpy as np

from class_item import Item
from champions.class_champion import Champion
import items.BRK as brk
import items.kraken_slayer as kraken_slayer
import champions.viego.scrapingViego as viego
import class_array
#import items.class_item

# %%
#Create a champion object containing a .stats attribute which is a dataframe
testChamp = viego.createViego()
print(testChamp.stats)
#Create a brk object
testBrk = brk.createBRK()
print(testBrk.stats)
#create a kraken object
testKraken = kraken_slayer.createKraken()

# Ajouter des éléments à testChamp
testChamp.addItem(testBrk)

testChamp.addItem(testKraken)


# Afficher les statistiques après l'ajout
print(testChamp.stats)


print("\n lalalala")
print(testChamp.choseLvl(4).index)
# %%
print(testBrk.stats)

# %%
print(testChamp.stats)

# %% [markdown]
# ## Test fonctionalities of class_array


# %%
testArray = class_array.Array()

# %%
testArray.append(testChamp.stats.columns, testChamp.choseLvl(5))

# %%
print(testArray)

# %%
