from centros import *
from departamentos import *
from cursos import *
from alunos_curso import *
from disciplinas_curso import *
from disciplinas_departamento import *

import requests
import json

from database_update import API

api = API("http://localhost:8081")

# CENTROS
cts = centros()
api.post(cts, "/centers")


# DEPARTAMENTOS
for centro in cts:
    deps = departamentos(centro['id'])

    api.post(deps, "/departments")


# CURSOS
todos_cursos = []
for centro in cts:
    crs = cursos(centro['id'])
    for c in crs:
        todos_cursos.append(c)

    api.post(crs, "/courses")


# ALUNOS
qtd_alunos = 0
for curso in todos_cursos:
    alunos = alunos_curso(curso['id'])

    api.post(alunos, "/students")


# delete from students;
# delete from centers;
# delete from departments;
# delete from courses;
