import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Infinity_Edge"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Trouver la section "Stats"
stats_section = soup.find('h2', {'class': 'pi-item pi-header pi-secondary-font pi-item-spacing pi-secondary-background'})

# Trouver les balises div suivantes
attack_damage_tag = stats_section.find_next('div', {'data-source': 'ad'})
crit_chance_tag = stats_section.find_next('div', {'data-source': 'crit'})
crit_damage_tag = stats_section.find_next('div', {'data-source': 'critdamage'})

# Extraire les informations
attack_damage = attack_damage_tag.text.strip() if attack_damage_tag else "Pas d'information sur les dégâts d'attaque."
crit_chance = crit_chance_tag.text.strip() if crit_chance_tag else "Pas d'information sur la chance de coup critique."
crit_damage = crit_damage_tag.text.strip() if crit_damage_tag else "Pas d'information sur les dégâts de coup critique."


def extract_numeric_value(text):
    # Utiliser une expression régulière pour extraire la première séquence de chiffres
    match = re.search(r'(\d+(\.\d+)?)', text)

    # Vérifier si une correspondance a été trouvée
    if match:
        numeric_value = float(match.group(1))
        
        # Vérifier si la valeur est précédée d'un pourcentage et la diviser par 100 si nécessaire
        if "%" in text:
            numeric_value /= 100

        return numeric_value
    else:
        return None
    
attack_damage = extract_numeric_value(attack_damage)
crit_chance = extract_numeric_value(crit_chance)
crit_damage = extract_numeric_value(crit_damage)

# Afficher les résultats
print(attack_damage)
print(crit_chance)
print(crit_damage)
