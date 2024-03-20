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
testBrk = brk.createBRK()
testKraken = kraken_slayer.createKraken()

# %%
print(testBrk)

# %%
#Create a champion object containing a .stats attribute which is a dataframe
viegoBRK = viego.createViego()
viegoBRK.addItem(testBrk)
viegoKraken = viego.createViego()
viegoKraken.addItem(testKraken)

# %% [markdown]
# ## Test fonctionalities of class_array


# %%
testArray = class_array.Array()

# %%
testArray.append(viegoBRK.stats.columns, viegoBRK.choseLvl(5))
testArray.append(viegoKraken.stats.columns, viegoKraken.choseLvl(6))

# %%
testArray.array


# %%
print(testArray.array['rMissingHealthDmg'])

# %%
testArray.array.columns

# %%
testArray.autoCalcul()
print(testArray.array['rMissingHealthDmg'])

# %%
