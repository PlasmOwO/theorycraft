import pandas as pd


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

def autoCalculColX(arrayBuild, nomCol : str):
    for idx, row in enumerate(arrayBuild[nomCol]):
        dictVar = {'BONUS_AD' : arrayBuild['ad'][idx] - arrayBuild['base_ad'][idx], 'TARGET_MISSING_HP' : 0.5}
        #dict ici mais global, va chercher la cellule N pour chaque var glob
        arrayBuild[nomCol][idx] = eval(row,dictVar)


class Array:
    def __init__(self):
        self.array = pd.DataFrame()
        
    def __str__(self):
        return self.array.to_string()
        
    def append(self,index,values):
        for col in index:
            if col not in self.array.columns:
                self.array[col] = 0
        new_row = pd.DataFrame([values], columns=index)

        self.array = pd.concat([self.array, new_row], ignore_index=True)

    
        #Ajoute au dataframe les colonnes nécessaires ainsi que les données
        ## Il faut prévoir une sorte de fonction qui ajoute des colonnes vides (0) dans le cas ou une des données n'est pas renseignée
        ## (exemple : si on a pas de degats on-hit, il faudra tout de meme une colonne dédié à cela)
        ## gérer aussi le cas de la brillance
    def autoCalcul(self):
        autoCalculColX(self.array,'rMissingHealthDmg')
        pass
        #Ajouter des colonnes
        #Automatiser le calcul de ses colonnes en fonction des valeurs brutes


