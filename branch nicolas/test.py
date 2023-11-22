import requests
from bs4 import BeautifulSoup

class ChampionScraper:
    def __init__(self, url):
        self.url = url
        self.soup = self.get_soup()

    def get_soup(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")

    def find_element_by_label(self, label, class_name):
        balise_h3 = self.soup.find('h3', class_='pi-data-label {}'.format(class_name), string=label)

        if balise_h3:
            balise_suivante = balise_h3.find_next_sibling()

            if balise_suivante:
                return balise_suivante.text.strip()

        return None

    def get_cooldown_value(self):
        return self.find_element_by_label('COOLDOWN:', 'pi-secondary-font')

    def get_bonus_physical_damage(self):
        balises_dl = self.soup.find_all('dl', class_='skill-tabs')
    
        for balise_dl in balises_dl:
            dt = balise_dl.find('dt')
            dd = balise_dl.find('dd')
            
            if dt and dd:
                texte = dd.find('span', style="color: #1F995C; white-space:normal")
        
        return texte

    def get_spell_range(self):
        ability_header_div = self.soup.find('div', {'class': 'champion-ability__header'})

        if ability_header_div:
            range_div = ability_header_div.find_next('div', {'data-source': 'range'})

            if range_div:
                range_value_tag = range_div.find('span', {'class': 'basic-tooltip'})

                if range_value_tag:
                    return range_value_tag.text.strip()

        return None

    def get_width_value(self):
        width_div = self.soup.find('div', {'data-source': 'width'})

        if width_div:
            width_value_tag = width_div.find('span', {'class': 'basic-tooltip'})

            if width_value_tag:
                return width_value_tag.text.strip()

        return None

    def Bonus_Damage(self):
        stats_div = self.soup.find('div', {'style': 'padding: 0 7px'})

        if stats_div:
            stats_dl_list = stats_div.find_all('dl', class_='skill-tabs')
            stats = {}

            for stats_dl in stats_dl_list:
                dt = stats_dl.find('dt')
                dd = stats_dl.find('dd')

                if dt and dd:
                    label = dt.text.strip().replace(':', '')
                    value = dd.text.strip()
                    stats[label] = value

            return stats

        return None

    def format_to_list(self, chaine):
        nombres = []
        nombre_temporaire = ""
        est_dans_nombre = False

        for caractere in chaine:
            if caractere.isdigit() or caractere == '.':
                nombre_temporaire += caractere
                est_dans_nombre = True
            elif est_dans_nombre:
                nombres.append(float(nombre_temporaire))
                nombre_temporaire = ""
                est_dans_nombre = False

        if est_dans_nombre:
            nombres.append(float(nombre_temporaire))

        return nombres

    def main(self):
        cooldown_value = self.get_cooldown_value()
        cooldown_value = self.format_to_list(cooldown_value)

        print("Cooldown\n")
        print(cooldown_value)
        print("\n")
        print("Spell Range")
        print(self.get_spell_range())
        print("\n")
        print("Width")
        print(self.get_width_value())
        print("\n")
        print("Bonus Damage Max/Min")
        print(self.Bonus_Damage())
        print("\n")
        print("Heartbreaker BONUS PHYSICAL DAMAGE")
        print(self.get_bonus_physical_damage()) 

if __name__ == "__main__":
    scraper = ChampionScraper("https://leagueoflegends.fandom.com/wiki/Viego/LoL")
    scraper.main()
