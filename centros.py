import requests
from bs4 import BeautifulSoup as soup


def centros():
    """
    centros retorna todos os centros de ensino da ufpb e seus 
    respectivos id's.
    """

    params = (
        ('aba', 'p-academico'),
    )

    response = requests.get(
        'https://sigaa.ufpb.br/sigaa/public/departamento/lista.jsf', params=params)

    page_soup = soup(response.content, "lxml")

    container = page_soup.find("select", {"id": "form:programas"})

    options = container.find_all("option")

    centros = [[centro['value'], centro.text] for centro in options]

    return centros
