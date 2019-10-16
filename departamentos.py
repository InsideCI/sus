import requests
from bs4 import BeautifulSoup as soup
# from centros import *


def departamentos(center_id):
    params = (
        ('lc', 'pt_BR'),
        ('id', center_id),
    )

    response = requests.get(
        'https://sigaa.ufpb.br/sigaa/public/centro/lista_departamentos.jsf', params=params)

    page_soup = soup(response.content, "lxml")

    try:
        listagem = page_soup.find("table", {"class": "listagem"})
    except:
        return []

    even = listagem.find_all("tr", {"class": "linhaPar"})
    odd = listagem.find_all("tr", {"class": "linhaImpar"})
    entries = even + odd

    deps = []

    for dep in entries:
        _, name = dep.a.text.strip().split(" - ")
        _, dep_id = dep.a['href'].split("id=")
        deps.append({"id": dep_id, "name": name, "center_id": center_id})

    return deps
