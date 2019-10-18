import requests
from bs4 import BeautifulSoup as soup


def professores_departamento(id_departamento):

    params = (
        ('id', id_departamento),
    )

    response = requests.get(
        'https://sigaa.ufpb.br/sigaa/public/departamento/professores.jsf', params=params)

    page_soup = soup(response.content, 'lxml')

    container = page_soup.find("div", {"id": "professores"})

    professores = container.find_all("table", {"align": "left"})

    profs = []

    for prof in professores:
        fields = prof.find_all("span")

        nome, grau = prof.find(
            "span", {"class": "nome"}).text.strip().split("(")
        nome = nome.strip()
        grau = grau[:-1]

        try:
            lattes = prof.find("span", {"class": "enderecoLattes"}).a['href']
        except:
            lattes = ''

        _, _id = prof.find("span", {"class": "pagina"}).a['href'].split("=")

        profs.append({"id": int(_id), "nome": nome, "grau": grau,
                      "id_departamento": int(id_departamento)})

    return profs
