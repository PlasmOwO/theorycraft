import pandas as pd


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
        pass
        #Ajouter des colonnes
        #Automatiser le calcul de ses colonnes en fonction des valeurs brutes

testArray = Array()

print(testArray)

idx = ['ad','as','ms','armor']

val = ['80','70','50','10']

testArray.append(idx,val)

print(testArray)


