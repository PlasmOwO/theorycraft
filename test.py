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
import items.Titanic_hydra as titanic_hydra
import items.black_cleaver as black_cleaver
import items.sundered_sky as sundered_sky
import items.triforce as triforce
import items.terminus as terminus

import champions.viego.scrapingViego as viego
import class_array
#import items.class_item

# %%
testBrk = brk.createBRK()
testKraken = kraken_slayer.createKraken()
testTitanic = titanic_hydra.createTitanic()
print(testTitanic)
testBC = black_cleaver.createBC()
testSunderedSky = sundered_sky.createSunderedSky()
testTriforce = triforce.createTriforce()
testTerminus = terminus.createTerminus()

# %%
print(testBrk)

# %%
#Create a champion object containing a .stats attribute which is a dataframe
viegoBRK = viego.createViego()
viegoBRK.addItem(testBrk)

viegoKraken = viego.createViego()
viegoKraken.addItem(testKraken)

viegoTitanic = viego.createViego()
viegoTitanic.addItem(testTitanic)
print(viegoTitanic)

#Not working
viegoBC = viego.createViego()
viegoBC.addItem(testBC)
viegoSundered = viego.createViego()
viegoSundered.addItem(testSunderedSky)

viegoTriforce = viego.createViego()
viegoTriforce.addItem(testTriforce)

viegoTerminus = viego.createViego()
viegoTerminus.addItem(testTerminus)



# %% [markdown]
# ## Test fonctionalities of class_array


# %%
testArray = class_array.Array()

# %%
testArray.append(viegoBRK.stats.columns, viegoBRK.choseLvl(6))
testArray.append(viegoKraken.stats.columns, viegoKraken.choseLvl(6))
testArray.append(viegoBC.stats.columns, viegoBC.choseLvl(6))
testArray.append(viegoSundered.stats.columns, viegoSundered.choseLvl(6))
testArray.append(viegoTriforce.stats.columns, viegoTriforce.choseLvl(6))
testArray.append(viegoTerminus.stats.columns, viegoTerminus.choseLvl(6))
testArray.append(viegoTitanic.stats.columns, viegoTitanic.choseLvl(6))

testArray.array['titanic_active_cleave'].replace(0,'0',inplace=True)
testArray.array['titanic_passive_cleave'].replace(0,'0',inplace=True)

# %%
testArray.array


# %%
print(testArray.array['qDoubletap'])

# %%
testArray.array['titanic_active_cleave']

# %%
testArray.array.columns

# %%
testArray.autoCalcul()
print(testArray.array['rMissingHealthDmg'])

# %%
testArray.array

# %%
testArray.array.iloc[6]

# %%
#rMissing health dmg = Depend des pv adverses
#qbrk, depend des pv
#Pour QautoDmg, wauto dmg ainsi que rdmg, il faut appliquer N fois les effets à l'impact
#Pour la cible, il faut lui choisir PV, ainsi que résistances, et faire un calcul via la pene.

#Calcul des dmg à l'impact (compliqué )
# Il faut dans un premier temps calculer les degats que fait BRK et passif Q
# Ensuite je dois créer une colonne qui additionne tous les ON HIT dammage. cependant si la colonne n'existe ps c chiant.
#Si deja je fais tous les objets on va etre vite régler je pense

# %% [markdown]
# * rMising health * PV
# * qbrk * 50% PV
# * passive * 50% PV

# %%
