import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup

br = RoboBrowser(parser='lxml')
br.open('https://sigaa.ufpb.br/sigaa/public/turmas/listar.jsf?aba=p-ensino')
form = br.get_form(id='formTurma')
#print(form)
form['formTurma:inputNivel'].value = 'G'
form['formTurma:inputDepto'].value = '2151'
form['formTurma:inputAno'] = '2019'
form['formTurma:inputPeriodo'].value = '2'
buscar = form['formTurma:j_id_jsp_1323203740_14']

br.submit_form(form, submit=buscar)

src = str(br.parsed())

page_soup = soup(src, "html.parser")

turmas = page_soup.findAll("span", {"class":"tituloDisciplina"})
for turma in turmas:
    print(turma.text)