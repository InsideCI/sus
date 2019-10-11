import requests
from bs4 import BeautifulSoup as soup
from centros import *

ctrs = centros()
for each in ctrs:
    print(each)

params = (
    ('nivel', 'G'),
    ('aba', 'p-ensino'),
)

response = requests.get(
    'https://sigaa.ufpb.br/sigaa/public/curso/lista.jsf', params=params)

page_soup = soup(response.content, "lxml")

listagem = page_soup.find("table", {"class": "listagem"})

options = listagem.find_all("tr")

centro_local = ""
centros = []
for tr in options:
    options = tr.find_all("td")

    centro = {}
    if len(options) == 1:  # É um centro
        centro_local = options[0].text.strip()
        continue  # Guarda o valor do centro, e passa pra o próximo curso
    if len(options) != 0:
        centro["id"] = options[-1].find("a")['href'][14:21]
        centro["nome"] = options[0].text.strip()
        centro["cidade"] = options[1].text.strip()
        centro["tipo"] = options[2].text.strip()
        centro["coordenador"] = options[3].text.strip()

    print(centro)

    # for each in options:
    #     print(each.text.strip(), end=" ")

    # link = options[len(options)-1]
    # print(link.find("a"))

    # print(" ", centro_local)
