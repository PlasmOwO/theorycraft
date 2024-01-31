# TODO LIST

## Objects

- [ ] Get all stats
- [ ] Reflexion for some difficulties (like Kraken slayer)
- [x] Store it into an object (named object...)
- [ ] Learning about new items coming for 2024

## Champions

- [ ] Get Viego's stats
- [ ] And spells (cd, dmg, ratio, scaling)
- [x] Store it into an object (create a class)
- [x] Create a method that add item to the champ (work to do)
    - [x] Add new cols if label not in base stats
    - [x] How to store dict into a pandas DataFrame (or maybe care about the index (lvl) and chose the right value)
    - [ ] Chose the right index of the dict based on index of DataFrame 
- [ ] Clean files

## Architecture

- [ ] Create a class that append line to a dataframe
- [ ] something like archi.add(ChampionWithBuildNumber1)
   - [ ] And display a new Pandas.DataFrame line
- [ ] Final state : Auto calcul columns based on the line created

-----------------------
Items scripts function to generate at the end the item based on the class.
Champs are just generated with class

So in the global script : import all classes, and items scripts one by one (to have data from scraping)

