#!/usr/bin/env python
# coding: utf-8
# %%

# # Class of items

# %%


class Item:
    def __init__(self, name : str, stats : dict):
        """
            Create an item object

            Params :
                name (str): Name of the object
                stats (dict) : Statistics of the object. Use the same keys for all your items.

        """
        self.name = name
        self.stats = stats

    def __str__(self):
        return self.name + " = "  + str(self.stats)


