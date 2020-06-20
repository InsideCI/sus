import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup


def disciplinasByCurso(course_id, year, period):

    br = RoboBrowser(parser='lxml')
    br.open(
        f"https://sigaa.ufpb.br/sigaa/public/curso/turmas.jsf?lc=pt_BR&id={course_id}")

    form = br.get_form(id='form')

    form['form:inputAno'] = year
    form['form:inputPeriodo'].value = period
    submit = form['form:j_id_jsp_771677251_40']
    br.submit_form(form, submit=submit)

    src = str(br.parsed())
    page_soup = soup(src, "html.parser")

    container = page_soup.find("div", {"id": "turmasAbertas"})
    tables = container.find_all("table")

    turmas = []

    for table in tables:
        disciplina = table.find("td", {"class": "subListagem"})
        disciplina = disciplina.text.strip().split(";")[-1]
        codigo, nome = disciplina.split(" - ")[:2]  # "CODIGO - DISCIPLINA"

        # EM CADA DISCIPLINA, ENCONTRE TODAS TURMAS
        tms = table.tbody.find_all("tr")

        for tm in tms:
            fields = tm.find_all("td")  # CAMPOS

            turma = fields[1].text.strip()
            professor = fields[2].text.strip().replace(
                "\t", "").replace("\n", "")
            horario = fields[4].text.strip()

            turmas.append({"id": codigo, "nome": nome, "turma": turma,
                           "professor": professor, "horario": horario,
                           "idCurso": int(course_id)})

    return turmas
