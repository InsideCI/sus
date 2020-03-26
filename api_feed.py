from scrappers.centros import *
from scrappers.departamentos import *
from scrappers.cursos import *
from scrappers.alunos_curso import *
from scrappers.professores_departamento import *

from utils.API import API

API_ADDRESS = "http://localhost:8080"
api = API(API_ADDRESS)

# CENTROS
cts = centros()
# api.post(cts, "/centers")

# DEPARTAMENTOS
# departments = []
# for centro in cts:
#     deps = departamentosByCentro(centro['id'])
#     for dep in deps:
#         print(dep)
#         departments.append(dep)
    # api.post(deps, "/departments")

# PROFESSORES
# for dep in departments:
#     teachers = professoresByDepartamento(dep['id'])
#     for teacher in teachers:
#         api.post(teacher, "/teachers")

# CURSOS
todos_cursos = []
for centro in cts:
    crs = cursosByCentro(centro['id'])
    for c in crs:
        # todos_cursos.append(c)

        api.post(c, "/courses")

# ALUNOS
# qtd_alunos = 0
# for curso in todos_cursos:
#     alunos = alunosByCurso(curso['id'])

# api.post(alunos, "/students")
