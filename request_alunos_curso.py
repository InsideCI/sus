import requests
from bs4 import BeautifulSoup as soup

def students_by_course(course_id):
    """
    alunos_curso retorna todos os alunos matriculados em um dado curso;
    
    params: (str) course_id -> ID do curso de acordo com o SIGAA UFPB.
    """

    params = (
    ('lc', 'pt_BR'),
    ('id', course_id),
    )

    response = requests.get('https://sigaa.ufpb.br/sigaa/public/curso/alunos.jsf', params=params)

    page_soup = soup(response.content, "lxml")

    container = page_soup.find("table", {"class":"listagem"})
    try:
        entry = container.find_all("tr")
    except:
        return []

    students = []

    for each in entry:
        raw = each.find_all("td")

        if len(raw) == 2:
            registration = raw[0].text
            name = raw[1].text

            students.append([registration, name])

    return students
