import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup

def alunos_curso(course_id):
    """
    alunos_curso retorna todos os alunos matriculados em um dado curso;
    
    params: (str) course_id -> ID do curso de acordo com o SIGAA UFPB.
    """

    br = RoboBrowser(parser='lxml')
    br.open(f'https://sigaa.ufpb.br/sigaa/public/curso/alunos.jsf?lc=pt_BR&id={course_id}')

    src = str(br.parsed())
    page_soup = soup(src, "html.parser")

    container = page_soup.find("table", {"class":"listagem"})
    raw_data = container.find_all("tr")

    students = [each.text.split('\n') for each in raw_data]
    students = students[:-1]
    
    for each in students:
        each = each[1:-1]
        each.append(course_id)
        print(each)

