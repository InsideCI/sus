from scrappers.centros import *
from scrappers.departamentos import *
from scrappers.cursos import *
from scrappers.alunos_curso import *

from utils.API import API

api = API("http://192.168.1.200:8081")

# CENTROS
cts = centros()
# api.post(cts, "/centers")


# DEPARTAMENTOS
for centro in cts:
    deps = departamentos(centro['id'])

    # api.post(deps, "/departments")


# CURSOS
todos_cursos = []
for centro in cts:
    crs = cursos(centro['id'])
    for c in crs:
        todos_cursos.append(c)

    # api.post(crs, "/courses")


# ALUNOS
qtd_alunos = 0
for curso in todos_cursos:
    alunos = alunos_curso(curso['id'])

    api.post(alunos, "/students")


# delete from students;
# delete from centers;
# delete from departments;
# delete from courses;
