import re
from robobrowser import RoboBrowser
from bs4 import BeautifulSoup as soup


def all_courses():
    br = RoboBrowser(parser='lxml')
    br.open('https://sigaa.ufpb.br/sigaa/public/curso/lista.jsf?nivel=G&aba=p-ensino')

    src = str(br.parsed())
    page_soup = soup(src, "html.parser")

    all_courses = list()    

    container = page_soup.find("table", {"class":"listagem"})
    raw_data = container.find_all("tr")
    ids = container.find_all('a')

    raw_data = raw_data[1:]

    for each in raw_data:
        each = each.text.replace('\t', '').strip().split('\n')
        each = list(filter(None, each))

        all_courses.append(each)


    all_courses = list(filter(lambda x: len(x) >1, all_courses))

    for i in range(0, len(ids)):
            s = ids[i]['href']
            result = re.search("id=(.+?)&", s)
            ids[i] = result.group(1)

    for i in range(0, len(ids)):
        all_courses[i].insert(0, ids[i])

    #print(all_courses)
    return all_courses
