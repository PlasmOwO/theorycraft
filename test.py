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
import matplotlib.pyplot as plt
from class_item import Item
from champions.class_champion import Champion
import items.BRK as brk
import seaborn as sns
import items.kraken_slayer as kraken_slayer
import items.Titanic_hydra as titanic_hydra
import items.black_cleaver as black_cleaver
import items.sundered_sky as sundered_sky
import champions.viego.scrapingViego as viego
import class_array
#import items.class_item

# %%
testBrk = brk.createBRK()
testKraken = kraken_slayer.createKraken()
testTitanic = titanic_hydra.createTitanic()
testBC = black_cleaver.createBC()
testSunderedSky = sundered_sky.createSunderedSky()

# %%
print(testBrk)

# %%
#Create a champion object containing a .stats attribute which is a dataframe
viegoBRK = viego.createViego()
viegoBRK.addItem(testBrk)
viegoKraken = viego.createViego()
viegoKraken.addItem(testKraken)
print(len(viegoKraken.stats))
viegoTitanic = viego.createViego()
viegoTitanic.addItem(viegoTitanic)
viegoTitanic.stats
#Not working
viegoBC = viego.createViego()
viegoBC.addItem(testBC)
viegoSundered = viego.createViego()
viegoSundered.addItem(testSunderedSky)


# %% [markdown]
# ## Test fonctionalities of class_array


# %%
testArray = class_array.Array()

# %%
testArray.append(viegoBRK.stats.columns, viegoBRK.choseLvl(6))
testArray.append(viegoKraken.stats.columns, viegoKraken.choseLvl(6))
testArray.append(viegoBC.stats.columns, viegoBC.choseLvl(6))
testArray.append(viegoSundered.stats.columns, viegoSundered.choseLvl(6))

testArray.array['titanic_active_cleave'].replace(0,'0',inplace=True)
testArray.array['titanic_passive_cleave'].replace(0,'0',inplace=True)

testArray.addEnnemyPlayer(1500,80)

# %%
testArray.array


# %%
print(testArray.array['qDoubletap'][2])

# %%
testArray.array.columns

# %%
testArray.autoCalcul()
print(testArray.array['rMissingHealthDmg'])

# %%
testArray.array

# %%
print(testArray.array['wCD'][0])
print(testArray.array['rCD'])

# %%
testArray.array.iloc[6]

# %%
finalArray = testArray.array[['hp','armor','magic_res','viegoPassiveRegen','lifesteal','burstDmg','DPS']]

# %%
finalArray

# %%
finalArrayNormalize = (finalArray - finalArray.min()) / (finalArray.max() - finalArray.min())

# %%
finalArrayNormalize

# %% [markdown]
# * BRK
# * Kraken
# * BC
# * Sundered
# * triforce
# * terminus
# * titanic

# %%
palette = sns.color_palette("husl", len(finalArrayNormalize))
num_vars = len(finalArrayNormalize.columns)

# Création d'un angle pour chaque variable
angles = [n / float(num_vars) * 2 * 3.14159 for n in range(num_vars)]
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Tracer un graphique radar pour chaque ligne de données
for i in range(len(finalArrayNormalize)):
    values = finalArrayNormalize.iloc[i].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=f'Item {i}', color=palette[i])

# Ajouter des étiquettes pour chaque variable
ax.set_xticks(angles[:-1])
ax.set_xticklabels(finalArrayNormalize.columns)

plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.show()

# %%
palette = sns.color_palette("husl", len(finalArrayNormalize))
num_vars = len(finalArrayNormalize.columns)

# Création d'un angle pour chaque variable
angles = [n / float(num_vars) * 2 * 3.14159 for n in range(num_vars)]
angles += angles[:1]

# Création des sous-graphiques pour chaque ligne
for i in range(len(finalArrayNormalize)):
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    
    values = finalArrayNormalize.iloc[i].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=1, linestyle='solid', label=f'Item {i}',color=palette[i])
    
    # Ajouter des étiquettes pour chaque variable
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(finalArrayNormalize.columns)
    
    # Ajouter une légende
    ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
    
    # Titre du graphique
    ax.set_title(f'Radar Plot - Item {i}')
    
    # Afficher le graphique
    plt.show()

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
# Il reste, imlémenter ON HIT
# Implémenter HP ennemy
# Implémenter RESI ennemy
# Implémenter tous les objets (notamment hydra qui bug)
