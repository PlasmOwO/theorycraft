#!/usr/bin/env python
# coding: utf-8
# %%

# # Class of champions
import numpy as np


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

    def createList(self, lvl : int):
        """
            Create a list from the index of the dataframe contained in the object.
        """
        pass #doit return une list (comme pour le excel)
        #Ensuite on ajoutera cette list au dataframe sur 1 champion
    


# %%
