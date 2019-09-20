import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup

def classes_course(course_id, year, period):

    br = RoboBrowser(parser='lxml')
    br.open(f"https://sigaa.ufpb.br/sigaa/public/curso/turmas.jsf?lc=pt_BR&id={course_id}")

    form = br.get_form(id='form')

    form['form:inputAno'] = year
    form['form:inputPeriodo'].value = period
    submit = form['form:j_id_jsp_771677251_40']
    br.submit_form(form, submit=submit)

    src = str(br.parsed())
    page_soup = soup(src, "html.parser")

    container = page_soup.find("div", {"id":"turmasAbertas"})
    tables = container.find_all("table")

    turmas = []

    for table in tables:
        disciplina = table.find("td", {"class":"subListagem"})
        disciplina = disciplina.text.strip().split(";")[-1] # Remoção de entulho JS
        codigo, nome = disciplina.split(" - ") # "CODIGO - DISCIPLINA"

        professores = table.find_all("td", {"class":"nome"})
        horarios = table.find_all("td", {"class":"horario"})

        # Pode haver mais de uma turma por disciplina;
        # A iteração abaixo serve para adicionar todas turmas
        # da mesma disciplina à lista de turmas.
        for professor, horario in zip(professores, horarios):
            turmas.append([codigo.replace("\n", ""),
            nome,
            professor.text.strip().replace("\t", "").replace("\n", ""),
            horario.text.strip()])


    return turmas

