import requests
from bs4 import BeautifulSoup
import re

url = "https://leagueoflegends.fandom.com/wiki/Titanic_Hydra"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Extraire Attack Damage
attack_damage_tag = soup.find('div', {'data-source': 'ad'})
attack_damage = re.search(r'\+(\d+(?:\.\d+)?)\s*attack damage', attack_damage_tag.text.strip()).group(1) if attack_damage_tag else "N/A"

# Extraire Health
health_tag = soup.find('div', {'data-source': 'hp'})
health = re.search(r'\+(\d+(?:\.\d+)?)\s*health', health_tag.text.strip()).group(1) if health_tag else "N/A"


div_elements = soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color')

# Définir un ensemble pour stocker temporairement les valeurs
unique_values = set()

# Parcourir les éléments et extraire les informations souhaitées
for div in div_elements[:4]:
    # Utilisez .find pour sélectionner le span avec la classe spécifiée à l'intérieur de chaque div
    data_value = div.find('div', class_='pi-data-value pi-font')

    if data_value:
        # Utiliser .find pour sélectionner le span avec le style spécifié à l'intérieur de data_value
        span_with_color = data_value.find('span', style='color: #1F995C; white-space:normal')

        if span_with_color:
            # Extraire le texte du span
            extracted_text = span_with_color.get_text(strip=True)
            
            # Appliquer l'expression régulière
            matches = re.finditer(r'\+?(\d+(?:\.\d+)?)%?', extracted_text)

            # Parcourir les correspondances
            for match in matches:
                # Si la correspondance a un pourcentage, l'ajouter à l'ensemble
                if '%' in match.group():
                    unique_values.add(match.group())

# Convertir l'ensemble en liste
result_list = list(unique_values)
def split_list(input_list):
    if len(input_list) != 4:
        raise ValueError("La liste doit contenir exactement 4 éléments.")

    # Extraire les extrémités
    extremes = [input_list[0], input_list[-1]]

    # Extraire la valeur du milieu
    middle_value = input_list[1:3]

    return extremes, middle_value

def process_percentage_list(input_list):
    processed_list = []

    for item in input_list:
        # Retirer le "%" et convertir en nombre décimal
        percentage_value = float(item.rstrip('%')) / 100.0
        processed_list.append(percentage_value)

    return processed_list

liste_passive_Titanic_hydra , list_active_Titanic_hydra = split_list(result_list)
liste_passive_Titanic_hydra = process_percentage_list(liste_passive_Titanic_hydra)
list_active_Titanic_hydra = process_percentage_list(list_active_Titanic_hydra)
print("Attack Damage:", attack_damage)
print("Health:", health) 

print(list_active_Titanic_hydra)
print("---------------")
print(liste_passive_Titanic_hydra)
