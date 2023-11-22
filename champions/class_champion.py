#!/usr/bin/env python
# coding: utf-8
# %%

# # Class of champions
import numpy as np


def extract_values(df):
    for col in df.columns:
        # Vérifier si la colonne contient des dictionnaires
        if all(isinstance(val, dict) for val in df[col]):
            values = []
            for index, row in df.iterrows():
                key = str(index + 1)
                value = row[col].get(key, None)

                if value is None:
                    # Si la clé n'existe pas, trouver la plus grande clé disponible
                    keys = [int(k) for k in row[col].keys() if k.isdigit() and int(k) < int(key)]
                    if keys:
                        max_key = str(max(keys))
                        value = row[col][max_key]

                values.append(value)
            df[col] = values


# %%
class Champion:
    def __init__(self, name : str, base_stats):
        self.name = name
        self.stats = base_stats

    def __str__(self):
        return self.name + "\n" + self.stats.to_string()
 

    def addItem(self,item):
        """
            Add an item to a champion
        """
        intersect = np.intersect1d(self.stats.columns.tolist(), list(item.stats.keys()))
        for col in intersect:
            self.stats[col] = [x+ item.stats[col] for x in self.stats[col]]
        newCols = [x for x in item.stats.keys() if x not in self.stats.columns.tolist()]
        for newCol in newCols :
            if type(item.stats[newCol]) == dict:
                self.stats[newCol] = [item.stats[newCol]] * self.stats.shape[0]
            else:
                self.stats[newCol] = item.stats[newCol]
        extract_values(self.stats)
    
    

    def createList(self, lvl : int):
        """
            Create a list from the index of the dataframe contained in the object.
        """
        pass #doit return une list (comme pour le excel)
        #Ensuite on ajoutera cette list au dataframe sur 1 champion
    


# %%
