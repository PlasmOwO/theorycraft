import requests
from bs4 import BeautifulSoup

url = "https://leagueoflegends.fandom.com/wiki/Viego/LoL"
response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")

def findSpan(typeTag: str, libTag: str):
    return html.find("span", {typeTag: libTag})

def statsort():
    return html.findAll('div', class_='pi-data-value pi-font')

def get_cooldown_value(html):
    # Analysez le HTML avec BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Recherchez la balise <h3> avec la classe spécifiée et le texte "COOLDOWN:"
    balise_h3 = soup.find('h3', class_='pi-data-label pi-secondary-font', text='COOLDOWN:')

    if balise_h3:
        # Obtenez la balise suivante (la ligne en dessous)
        balise_suivante = balise_h3.find_next_sibling()

        if balise_suivante:
            # Récupérez le texte de la balise suivante
            contenu = balise_suivante.text.strip()
            return contenu
    return None

def main():
    print("\n")
    print("Résultat du scraping : \n")
    
    # Appel de la fonction get_cooldown_value
    cooldown_value = get_cooldown_value(response.text)

    if cooldown_value:
        print("Cooldown:", cooldown_value)
    else:
        print("COOLDOWN non trouvé.")

if __name__ == "__main__":
    main()
