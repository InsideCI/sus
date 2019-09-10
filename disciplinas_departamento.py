import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup

def classes_and_teachers_dep(nivel, departamento, ano, periodo):

    br = RoboBrowser(parser='lxml')
    br.open('https://sigaa.ufpb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino')

    # Filling form for Class search
    form = br.get_form(id='formTurma')
    form['formTurma:inputNivel'].value = nivel
    form['formTurma:inputDepto'].value = departamento
    form['formTurma:inputAno'] = ano
    form['formTurma:inputPeriodo'].value = periodo
    buscar = form['formTurma:j_id_jsp_1323203740_14']

    br.submit_form(form, submit=buscar)

    src = str(br.parsed())
    page_soup = soup(src, "html.parser")

    container = page_soup.find("table", {"class":"listagem"})
    raw_data = container.find_all("tr")

    # Unwanted page data
    raw_data = raw_data[1:-1]

    teachers_and_classes = list(each.text.strip().split("\n") for each in raw_data)
    teachers_and_classes[0] = [teachers_and_classes[0][-1]] # Removing useless server data

    return teachers_and_classes


