import requests
from bs4 import BeautifulSoup
import re

url = 'https://en.wikipedia.org/wiki/List_of_Greek_mythological_figures'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

name_english = []
name_greek = []
t = []
t_sub = []
description = []

# Major Gods
major = soup.find_all('table', {'class': 'wikitable',
                                'width': '100%'})
for tr in major[0].find_all('tr')[1:]:
    name_e = tr.find('b')
    name_g = tr.find('span', {'lang': 'grc'})
    d = tr.find('p')

    name_english.append(name_e.text)
    name_greek.append(name_g.text)
    t.append('god')
    t_sub.append('olympian')
    description.append(d.text)

# Primordial Gods
primordial = soup.find_all('table', {'class': 'wikitable',
                                     'style': 'border'})
for tr in primordial[0].find_all('tr')[1:]:
    name_g = tr.find('span', {'lang': 'grc'})
    name_e = tr.find('a')
    d = name_e.find_next('td')

    name_english.append(name_e.text)
    name_greek.append(name_g.text)
    t.append('god')
    t_sub.append('primordial')
    description.append(d.text)

# Titans and Titanesses
titans = soup.find_all('table', {'class': 'wikitable',
                                 'cellpadding': '6'})
for tr in titans[0].find_all('tr')[2:14]:
    name_g = tr.find('span', {'lang': 'grc'})
    name_e = tr.find('a')
    d = name_e.find_next('td')

    name_english.append(name_e.text)
    name_greek.append(name_g.text)
    t.append('titan')
    t_sub.append('twelve titan')
    description.append(d.text)
for tr in titans[0].find_all('tr')[15:]:
    name_g = tr.find('span', {'lang': 'grc'})
    name_e = tr.find('a')
    d = name_e.find_next('td')

    name_english.append(name_e.text)
    name_greek.append(name_g.text)
    t.append('titan')
    t_sub.append('other titan')
    description.append(d.text)

# Other Gods
others = soup.find_all(
    'div', {'class': 'div-col columns column-width',
            'style': '-moz-column-width: 30em; '
                     '-webkit-column-width: 30em; '
                     'column-width: 30em;'})

concepts = others[0]
for li in concepts.find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('personification')
    t_sub.append('personification')
    description.append(d)

chthonic = others[1]
for li in chthonic.find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('god')
    t_sub.append('chthonic')
    description.append(d)

sea = soup.find_all(
    'div', {'class': 'div-col columns column-width',
            'style': '-moz-column-width: 35em; '
                     '-webkit-column-width: 35em; '
                     'column-width: 35em;'})
for li in sea[0].find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('god')
    t_sub.append('sea')
    description.append(d)

sky = others[2]
for li in sky.find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('god')
    t_sub.append('sky')
    description.append(d)

rustic = others[3]
for li in rustic.find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('god')
    t_sub.append('rustic')
    description.append(d)

agriculture = others[4]
for li in agriculture.find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('god')
    t_sub.append('agriculture')
    description.append(d)

health = others[5]
for li in health.find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('god')
    t_sub.append('health')
    description.append(d)

sleep = others[6]
for li in sleep.find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('god')
    t_sub.append('sleep')
    description.append(d)

other = others[7]
for li in other.find_all('li'):
    gods = li.text
    name_g = re.findall(r'\(\s*(.+)\)', gods)
    name_e = re.findall(r'^(.*)\s\(', gods)
    d = re.findall(r'\),*\s(.*)', gods)

    name_english.append(name_e)
    name_greek.append(name_g)
    t.append('god')
    t_sub.append('other')
    description.append(d)