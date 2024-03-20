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

# +
#'BONUS_AD' : arrayBuild['ad'][idx] - arrayBuild['base_ad'][idx], 'TARGET_MISSING_HP' : 0.5,
#, 'BONUS_AS' : arrayBuild['as'], 'AP' : '0.0'
# -

def autoCalculColX(arrayBuild, nomCol : str):
    for idx, row in enumerate(arrayBuild[nomCol]):
        dictVar = {'BONUS_AD' : arrayBuild['ad'][idx] - arrayBuild['base_ad'][idx], 'TARGET_MISSING_HP' : 0.5, 'CRIT_CHANCE': arrayBuild['crit'][idx],'critical strike chance': arrayBuild['crit'][idx], 'BONUS_AS' : arrayBuild['as'][idx], 'AP' : 0.0, 'AD' : arrayBuild['ad'][idx], "HP" : arrayBuild['hp'][idx]}
        #dict ici mais global, va chercher la cellule N pour chaque var glob
        arrayBuild[nomCol][idx] = eval(row,dictVar)


# testPandas = pd.DataFrame({'crit': ['0','0.2'] , 'target' : ['120 * (1 + CRIT_CHANCE )','120 * (1 + CRIT_CHANCE )']})
# testPandas
#

# eval("120 * ( 1 + CRIT_CHANCE)",{ 'CRIT_CHANCE': 0.0})
# #autoCalculColX(testPandas,'target')

# 0 120.0 1 144.0 Name: crit, dtype: float64

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
        self.array.fillna(0, inplace=True)

        #formula = RATIO = 0.658,  Formule total AS : *TOTAL = base + ratio*bonus
        self.array['as_per_second'] = self.array['base_as'] + 0.658*self.array['as']
        autoCalculColX(self.array,'rMissingHealthDmg')
        autoCalculColX(self.array,'rAutoDmg')
        autoCalculColX(self.array,'qActive')
        autoCalculColX(self.array,'qDoubletap')
        autoCalculColX(self.array,'wDmg')
        autoCalculColX(self.array,'viegoPassiveRegen')
        #autoCalculColX(self.array,'titanic_passive')
        #autoCalculColX(self.array,'titanic_active')


        # 0.625 × (1 + 97.35 ÷ 100)
        self.array['qAutoDmg'] = self.array['qActive'] + self.array['ad'] + self.array['qDoubletap']
        self.array['wAutoDmg'] = self.array['wDmg'] + self.array['ad'] + self.array['qDoubletap']
        self.array['rTotalDmg'] = self.array['rAutoDmg'] + self.array['rMissingHealthDmg']
          #Ajouter des colonnes
        #Automatiser le calcul de ses colonnes en fonction des valeurs brutes



# +
# e-z auto q-auto R
# degats du Q / cd
# degats du W / cd 
# dmg du R / cd
# nombre d'attaque par seconde
# -


