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

    for table in tables:
        nome = table.find("td", {"class":"nome"})
        horario = table.find("td", {"class":"horario"})

        print(nome.text.strip().replace("\t", "").replace("\n", ""), horario.text.strip())


classes_course("1626865", "2019", "1")