from scrappers.centros import centros
from scrappers.cursos import cursosByCentro
from scrappers.departamentos import departamentosByCentro
from scrappers.professores_departamento import professoresByDepartamento
from scrappers.alunos_curso import alunosByCurso
from scrappers.disciplinas_curso import disciplinasByCurso

ID_CENTROINFORMATICA = "1856"
ID_ENGENHARIA = "1626865"
ID_DEPARTAMENTOINFORMATICA = "2151"

ANO = "2019"
PERIODO = "2"

## CENTROS
# centers = centros()
# for center in centers:
#     print(center)

## DEPARTAMENTOS
# departamentos = departamentosByCentro(ID_CENTROINFORMATICA)
# for departamento in departamentos:
#     print(departamento)

## PROFESSORES
# professores = professoresByDepartamento(ID_DEPARTAMENTOINFORMATICA)
# for professor in professores:
#     print(professor)

## CURSOS
# courses = cursosByCentro(ID_CENTROINFORMATICA)
# for course in courses:
#     print(course)

## ALUNOS
# students = alunosByCurso(ID_ENGENHARIA)
# for student in students:
#     print(student)

## DISCIPLINAS
disciplinas = disciplinasByCurso(ID_ENGENHARIA, ANO, PERIODO)
for disciplina in disciplinas:
    print(disciplina)