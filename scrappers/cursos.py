import requests
from bs4 import BeautifulSoup as soup
# from centros import *


def cursosByCentro(center_id):
    """
    cursos returns all courses based on relative to some center.

    params:
    string center_id -> expects a valid UFPB center ID.
    """
    params = (
        ('lc', 'pt_BR'),
        ('id', center_id),
    )

    response = requests.get(
        'https://sigaa.ufpb.br/sigaa/public/centro/lista_cursos.jsf', params=params)

    page_soup = soup(response.content, "lxml")

    listagem = page_soup.find("table", {"class": "listagem"})

    try:
        even = listagem.find_all("tr", {"class": "linhaPar"})
        odd = listagem.find_all("tr", {"class": "linhaImpar"})
        entries = even + odd
    except:
        return []

    courses = []

    for course in entries:
        fields = course.find_all("td")

        _, course_id = fields[-1].a['href'].split("id=")
        city = fields[1].text.strip()
        name = fields[0].text.strip().replace(" - " + city, "")
        _type = fields[2].text.strip()
        coordinator = fields[3].text.strip()

        courses.append({"id": int(course_id), "nome": name, "cidade": city, "tipo": _type,
                        "coordenador": coordinator, "idCentro": int(center_id)})

    return courses
