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
import champions.viego.scrapingViego as viego
import class_array
#import items.class_item

# %%
testChamp = viego.createViego()
testBrk = brk.createBRK()

# Ajouter des éléments à testChamp
testChamp.addItem(testBrk)

# Afficher les statistiques après l'ajout
print(testChamp.stats)


print("\n lalalala")
print(testChamp.choseLvl(4).index)
# %% [markdown]
# ## Test fonctionalities of class_array


# %%
testArray = class_array.Array()

# %%
testArray.append(testChamp.stats.columns, testChamp.choseLvl(5))

# %%
print(testArray)

# %%
