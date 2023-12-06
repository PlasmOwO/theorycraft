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
    
    def get_soup(self):
        response = requests.get(self.url)
        return BeautifulSoup(response.text, "html.parser")
    
    '''
    extrait le text sans balise
    '''
    def extract_text_without_tags(self, element):
        """
        Extract text content from HTML without any tags.
        """
        result = []
        for item in element.children:
            if isinstance(item, str):
                if item != "\n":
                    result.append(item)
            else:
                result += self.extract_text_without_tags(item)

        return result

    def get_divs_above_img(self, img_alt_text):
        img_tag = self.soup.find('img', alt=img_alt_text)

        if img_tag:
            parent_div = img_tag.find_parent('div')
            divs_above = parent_div.find_all_previous('div', limit=1)

            return divs_above

        return None
    def get_orange_and_blue_text(self, divs_above_img):
        # color #7A6DFF bleu et orange
        orange_and_blue_text = []

        for div in divs_above_img:
            orange_text = div.find_all('span', style="color:orange; white-space:normal",limit=2)
            blue_text = div.find_all('span', style="color: #7A6DFF; white-space:normal")

            for text in orange_text:
                orange_and_blue_text.append(text.get_text(strip=True))

            for text in blue_text:
                orange_and_blue_text.append(text.get_text(strip=True))

        return orange_and_blue_text
    
    def find_physical_damage_table(self):
        physical_damage_span = self.soup.find('span', {'class': 'template_lc'}, string='Physical Damage:')
        if physical_damage_span:
            table = physical_damage_span.find_previous('table')
            dd_elements = table.find('dd', class_='')
            dd_texts = [dd.get_text(strip=True) for dd in dd_elements]

        return dd_texts
    
    def find_physical_damage_span(self):
        return self.soup.find('span', {'class': 'template_lc'}, string='Physical Damage:')
    
    
    def main(self):
        cooldown_value = self.get_cooldown_value()
        cooldown_value = self.format_to_list(cooldown_value)

        print("Cooldown\n")
        print(cooldown_value)
        print("\n")
        print("Bonus Damage Max/Min")
        print(self.Bonus_Damage())
        print("\n")
        print("Heartbreaker BONUS PHYSICAL DAMAGE")
        print(self.get_bonus_physical_damage()) 
        print("\n")
        print("bonus damage 2")
        img_alt_text = 'Blade of the Ruined King'
        divs_above_img = self.get_divs_above_img(img_alt_text)
        if divs_above_img:
            orange_and_blue_text = self.get_orange_and_blue_text(divs_above_img)
            print(orange_and_blue_text)
        physical_damage_table = self.find_physical_damage_table()
        if physical_damage_table:
            print("\nPhysical Damage Table:")
            print(physical_damage_table)



if __name__ == "__main__":
    scraper = ChampionScraper("https://leagueoflegends.fandom.com/wiki/Viego/LoL")
    scraper.main()
