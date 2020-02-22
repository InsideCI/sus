import requests
from bs4 import BeautifulSoup as soup


def professoresByDepartamento(id_departamento):
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
        try:
            nome, grau = prof.find(
                "span", {"class": "nome"}).text.strip().split("(")
            grau = grau[:-1]
        except ValueError:
            nome = prof.find(
                "span", {"class": "nome"}).text.strip()
            grau = ''

        nome = nome.strip()

        _, _id = prof.find("span", {"class": "pagina"}).a['href'].split("=")

        profs.append({"id": int(_id), "nome": nome, "grau": grau,
                      "idDepartamento": int(id_departamento)})

    return profs
