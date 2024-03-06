# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Web scraping stat Viego

import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


url = "https://leagueoflegends.fandom.com/wiki/Viego/LoL"
url

# *Statistic growth = base+ (perlvl) x (n-1) x (0.7025 + 0.0175 x (n-1))*

response = requests.get(url)
html = BeautifulSoup(response.text, "html.parser")


def findSpan(typeTag : str,  libTag : str):
    return html.find("span", {typeTag : libTag})


hp = findSpan("id","Health_Viego")
hp_lvl = findSpan("id","Health_Viego_lvl")
hp_list = [(float(hp.text) + float(hp_lvl.text) * (n-1) *(0.7025 +0.0175 * (n-1))) for n in range(1,19)]

armor =  findSpan("id","Armor_Viego")
armor_lvl = findSpan("id","Armor_Viego_lvl")
armor_list = [(float(armor.text) + float(armor_lvl.text) * (n-1) *(0.7025 +0.0175 * (n-1))) for n in range(1,19)]

rm = findSpan("id","MagicResist_Viego")
rm_lvl = findSpan("id","MagicResist_Viego_lvl")
rm_list = [(float(rm.text) + float(rm_lvl.text) * (n-1) *(0.7025 +0.0175 * (n-1))) for n in range(1,19)]

ad = findSpan("id","AttackDamage_Viego")
ad_lvl = findSpan("id","AttackDamage_Viego_lvl")
ad_list = [(float(ad.text) + float(ad_lvl.text) * (n-1) *(0.7025 +0.0175 * (n-1))) for n in range(1,19)]

attack_speed = html.findAll('div', {"style" : "width: calc(1 / 2 * 100%);"})
attack_speed = attack_speed[10]
attack_speed = float(re.sub(r'[^0-9.,]', '', attack_speed.text))

bonus_as_lvl = html.findAll('div', {"style" : "width: calc(1 / 2 * 100%);"})
bonus_as_lvl = bonus_as_lvl[13]
bonus_as_lvl = float(re.sub(r'[^0-9.,]', '', bonus_as_lvl.text))
bonus_as_lvl /=100
bonus_as_list = [ float(bonus_as_lvl) * (n-1) *(0.7025 +0.0175 * (n-1)) for n in range(1,19)]

# RATIO = 0.658
# Formule total AS : *TOTAL = base + ratio*bonus

ratio = 0.658

as_list = [ attack_speed + ratio*bonus_as_list[n]  for n in range(0,18)]


viegoStat = pd.DataFrame(index=range(1,19),columns=['hp','armor','magic_res','ad','as'])
viegoStat['hp'] = hp_list
viegoStat['armor'] = armor_list
viegoStat['magic_res'] = rm_list
viegoStat['ad'] = ad_list
viegoStat['as'] = bonus_as_list #Ici c'est le bonus d'attaque speed, il faut additionner les autres bonus


# ## Scraping passive and W

pViego = html.find("div" ,{'class' : 'skill skill_innate' })
wViego = html.find("div", {"class" : "skill skill_w"})

# +
pViegoList = []
try :
    pViegoList.append(str(float(re.sub(r'[^0-9.,]', '', pViego.find("span", {'style' : "color: #1F995C; white-space:normal"}).text))/100))
    
    pViegoList.append(str(float(re.sub(r'[^0-9.,]', '',pViego.find("span",{"style" : "color:orange; white-space:normal"}).text[0:10]))/10000) +"BONUS_AD")
    
    pViegoList.append(str(float(re.sub(r'[^0-9.,]', '',pViego.find("span",{"style" : "color: #7A6DFF; white-space:normal"}).text[0:10]))/10000)+"AP")
    
    pViegoList.append(str(float(re.sub(r'[^0-9.,]', '',pViego.find("span",{"style" : "color:orangered; white-space:normal"}).text[0:10]))/10000)+"BONUS_AS")

    
    wViegoCD = wViego.find("div",{"class" : "pi-data-value pi-font"}).text # W cd

except AttributeError:
    print("error")

wViegoRatio = str(int(re.sub(r'[^0-9.,]','',re.search(r'\(([^)]+)\)', wViego.find("dd").text).group(1) if re.search(r'\(([^)]+)\)', wViego.find("dd").text) else None))/100) + "AP"
wViegoDmg = list(map(int,re.sub(r'\([^)]+\)', '', wViego.find("dd").text).split("/")))


wViegoAll = [str(x)+"+"+wViegoRatio for x in wViegoDmg]


# -

# ## Scraping Q spell

# +

def find_element_by_label(label, class_name):
    if html is None:
        return None

    balise_h3 = html.find('h3', class_='pi-data-label {}'.format(class_name), string=label)

    if balise_h3:
        balise_suivante = balise_h3.find_next_sibling()

        if balise_suivante:
            return balise_suivante.text.strip()


def get_cooldown_value():
    return find_element_by_label('COOLDOWN:', 'pi-secondary-font')

def Bonus_Damage():
    stats_div = html.find('div', {'style': 'padding: 0 7px'})

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

def format_to_list(chaine):
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

'''
extrait le text sans balise
'''
def extract_text_without_tags(element):
    """
    Extract text content from HTML without any tags.
    """
    result = []
    for item in element.children:
        if isinstance(item, str):
            if item != "\n":
                result.append(item)
        else:
            result += html.extract_text_without_tags(item)

    return result

def get_divs_above_img(img_alt_text):
    img_tag = html.find('img', alt=img_alt_text)

    if img_tag:
        parent_div = img_tag.find_parent('div')
        divs_above = parent_div.find_all_previous('div', limit=1)

        return divs_above

    return None
def get_orange_and_blue_text(divs_above_img):
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

def find_physical_damage_table():
    physical_damage_span = html.find('span', {'class': 'template_lc'}, string='Physical Damage:')
    if physical_damage_span:
        table = physical_damage_span.find_previous('table')
        dd_elements = table.find('dd', class_='')
        dd_texts = [dd.get_text(strip=True) for dd in dd_elements]

    return dd_texts

def find_physical_damage_span():
    return html.find('span', {'class': 'template_lc'}, string='Physical Damage:')


#Scraping viego Q spell
cooldown_value = get_cooldown_value()
cooldown_value = format_to_list(cooldown_value)



qPassiveBRKdmgList = [int(x) /100 for x in re.findall(r'\d+', Bonus_Damage()['Bonus Physical Damage'])]

img_alt_text = 'Blade of the Ruined King'
divs_above_img = get_divs_above_img(img_alt_text)
if divs_above_img:
    orange_and_blue_text = get_orange_and_blue_text(divs_above_img)
physical_damage_table = find_physical_damage_table()

qActiveDMGList =  physical_damage_table[0].split(" / ")
#QactiveRatio
qActiveRatio = re.findall(r'\d+', physical_damage_table[1])
#WARNING THIS VALUE IS FLAT ENTRY
qActiveRatio = str([int(x) /100 for x in qActiveRatio][0]) + "AD" + ")x(1+CRIT_CHANCE)"

qActiveDMG = []
for i in range(len(qActiveDMGList)):
    qActiveDMG.append("(" + qActiveDMGList[i] + "+" + qActiveRatio)


# Double tap dmg q passive


doubletap_nocrit= "(" +str(int(re.findall(r'\d',orange_and_blue_text[0])[0])/100) + "+" +str(int(re.findall(r'\d+',orange_and_blue_text[2])[0])/100)+ "AP)AD" 

# -

# ## Q processing

# +
#qCD into stats tab
indexLvl = range(1,19)
qCDval = []
qCDval += [cooldown_value[0]] * 3
qCDval += [cooldown_value[1]] *1
qCDval += [cooldown_value[2]] *2
qCDval += [cooldown_value[3]] *2
qCDval += [cooldown_value[4]] *10

qCD = dict(map(lambda i,j : (i,j) , indexLvl,qCDval))


# +
#qPassiveBRK
qBRKval = []

qBRKval += [qPassiveBRKdmgList[0]] * 3
qBRKval += [qPassiveBRKdmgList[1]] *1
qBRKval += [qPassiveBRKdmgList[2]] *2
qBRKval += [qPassiveBRKdmgList[3]] *2
qBRKval += [qPassiveBRKdmgList[4]] *10
qBRK = dict(map(lambda i,j : (i,j) , indexLvl,qBRKval))
# -

#qActiveDmg
qActiveDmgVal = []
qActiveDmgVal += [qActiveDMG[0]] * 3
qActiveDmgVal += [qActiveDMG[1]] *1
qActiveDmgVal += [qActiveDMG[2]] *2
qActiveDmgVal += [qActiveDMG[3]] *2
qActiveDmgVal += [qActiveDMG[4]] *10
qActive = dict(map(lambda i,j : (i,j) , indexLvl,qActiveDmgVal))

# ## W processing

# +
wDmgval = []

wDmgval += [0] * 1
wDmgval += [wViegoAll[0]] *13
wDmgval += [wViegoAll[1]] *1
wDmgval += [wViegoAll[2]] *2
wDmgval += [wViegoAll[3]] *1
wDmgval += [wViegoAll[4]] *1
wDmg = dict(map(lambda i,j : (i,j) , indexLvl,wDmgval))

# +
# QWEQQRQEQEREEWWRWW
# -

# ## Ultime Viego  

# Ultime Cooldown 

# +
soup = BeautifulSoup(response.content, 'html.parser')

ultime_cooldown = soup.find("div", {'class': 'skill skill_r'})
if ultime_cooldown:
    ultime_cooldown_value = ultime_cooldown.find('div', {'class': 'pi-data-value pi-font'})
    if ultime_cooldown_value:
        ultime_cooldown_text = ultime_cooldown_value.text
    else:
        print('Element "pi-data-value pi-font" non trouvé dans skill_r')
else:
    print('Element "skill skill_r" non trouvé dans la page')
# -

# Base attack during ultimate

soup = BeautifulSoup(response.content, 'html.parser')
lr = soup.find("div", {'class' : 'skill skill_r'})
lr = lr.find('span', {'class' : 'pp-tooltip'})['data-displayformula']

# Physical Damage

soup = BeautifulSoup(response.content, 'html.parser')
pdamage = soup.find("div", {'class': 'skill skill_r'})
pdamage = pdamage.find('div', {'style': 'grid-column-end: span 2; display:contents'})
pdamage = pdamage.find('span', {'style': 'color: #1F995C; white-space:normal'})

# Clean data entries

# +
#Divide string using (
before_parenthese = re.match(r'^(.*?)\(', pdamage.text).group(1) if re.match(r'^(.*?)\(', pdamage.text) else None
after_parenthese = re.search(r'\(.*\)', pdamage.text).group(0) if re.search(r'\(.*\)', pdamage.text) else None

#Delete % in the first string, and split
before_parenthese_without= re.sub(r'%', '', before_parenthese)
R_missing_health_dmg = before_parenthese_without.split(" / ")
R_missing_health_dmg = [int(x)/100 for x in R_missing_health_dmg]
R_missing_health_dmg = [float(x) for x in R_missing_health_dmg]

#Delete % in the second string and add it to another col
### after_parenthese = re.sub(r'%','',after_parenthese)
# -

# Stat board

UltimeStat = pd.DataFrame(index=range(1,4))
UltimeStat['Ultimate_cooldown'] = ultime_cooldown_text.split(" / ")
UltimeStat['R_Physical_missing_health_damages'] = R_missing_health_dmg
UltimeStat['R_Physical_missing_health_damages'] = UltimeStat['R_Physical_missing_health_damages']
UltimeStat['R_missing_health_ratio'] = str(int(re.sub(r'[^0-9.,]','',after_parenthese[0:9]))/10000) + "BONUS_AD"
UltimeStat['R_auto_dmg'] = lr
UltimeStat

# Creation object

if __name__ == "__main__":
    import sys
    sys.path.append("..")
    from class_champion import Champion
else :
    from champions.class_champion import Champion
import copy

# +
viegoStat['rCD'] = 0
viegoStat['rMissingHealthDmg'] = 0
viegoStat['rAutoDmg'] = 0
viegoStat['qCD'] = qCD
viegoStat['qBRK'] = qBRK
viegoStat['qActive'] = qActive
viegoStat['wDmg'] = wDmg
for i in range (6,11):
    viegoStat['rCD'][i] = UltimeStat['Ultimate_cooldown'][1]
    viegoStat['rMissingHealthDmg'][i] = str(UltimeStat['R_Physical_missing_health_damages'][1])+ "+" + UltimeStat['R_missing_health_ratio'][1] + "TARGET_MISSING_HP"
    viegoStat['rAutoDmg'][i] = UltimeStat['R_auto_dmg'][1]
for i in range (11,16):
    viegoStat['rCD'][i] = UltimeStat['Ultimate_cooldown'][2]
    viegoStat['rMissingHealthDmg'][i] = str(UltimeStat['R_Physical_missing_health_damages'][2])+ "+" + UltimeStat['R_missing_health_ratio'][2] + "TARGET_MISSING_HP"
    viegoStat['rAutoDmg'][i] = UltimeStat['R_auto_dmg'][1]

for i in range  (16,19):
    viegoStat['rCD'][i] = UltimeStat['Ultimate_cooldown'][3]
    viegoStat['rMissingHealthDmg'][i] = str(UltimeStat['R_Physical_missing_health_damages'][3])+ "+" + UltimeStat['R_missing_health_ratio'][3] + "TARGET_MISSING_HP"
    viegoStat['rAutoDmg'][i] = UltimeStat['R_auto_dmg'][1]

viegoStat['viegoPassiveRegen'] = "+".join(pViegoList)
viegoStat['wCD'] = wViegoCD
viegoStat['qDoubletap'] = doubletap_nocrit
viegoStat['base_ad'] = viegoStat['ad']
viegoStat['base_hp'] = viegoStat['hp']

viegoBase = Champion("viego",viegoStat)


# -

def createViego():
    stats = viegoStat.copy()
    return Champion("viego", stats)


createViego().stats


