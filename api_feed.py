from scrappers.centros import *
from scrappers.departamentos import *
from scrappers.cursos import *
from scrappers.alunos_curso import *
from scrappers.professores_departamento import *
from scrappers.disciplinas_curso import disciplinasByCurso

from utils.API import API

API_ADDRESS = "https://cinside.ddns.net:8081"
api = API(API_ADDRESS)

# CENTROS
print("Getting centers")
cts = centros()
# for ct in cts:
#     api.post(ct, "/centers")

# # DEPARTAMENTOS
# print("Getting departments")
# departments = []
# for centro in cts:
#     deps = departamentosByCentro(centro['id'])
#     for dep in deps:
#         departments.append(dep)
#         api.post(dep, "/departments")

# # PROFESSORES
# print("Getting teachers")
# for dep in departments:
#     teachers = professoresByDepartamento(dep['id'])
#     for teacher in teachers:
#         api.post(teacher, "/teachers")

# # CURSOS
print("Getting courses")
courses = []
for centro in cts:
    crs = cursosByCentro(centro['id'])
    for c in crs:
        courses.append(c)
#         # api.post(c, "/courses")

# # # ALUNOS
# print("Getting students")
# for course in courses:
#     alunos = alunosByCurso(course['id'])
#     for aluno in alunos:
#         api.post(aluno, "/students")


print("Getting classes")
for course in courses:
    disciplinas = disciplinasByCurso(course['id'], "2019", "2")
    for disciplina in disciplinas:
        api.post(disciplina, "/classes")
