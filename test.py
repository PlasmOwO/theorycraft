# %%
# utiliser sys.path

# Script : Faire une fonction qui **return** un objet Item

import pandas as pd
import numpy as np

from class_item import Item
import items.BRK as brk
#import items.class_item

# %%
print(brk.createBRK(False))

print(brk.createBRK())

from champions.class_champion import Champion

dfTest = pd.DataFrame({'ad' : range(500,1000,100)})

dfTest

testChamp =Champion("viego",dfTest)

print(testChamp)

testBrk = brk.createBRK()
print(testBrk.stats['ad'])

# On veut que la fonction addItem, additionne, parmis les colonnes commune (label) toutes les lignes de cette colonne par la stat de l'objet

import numpy as np

testChamp.addItem(testBrk)

print(testChamp)
# %%

