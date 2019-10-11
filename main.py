from centros import *
from departamentos import *
from cursos_ufpb import *
from alunos_curso import *
from disciplinas_curso import *
from disciplinas_departamento import *

import requests
import json


# 1859 - DEPARTAMENTO DE COMPUTAÇÃO CIENTÍFICA
# 2151 - DEPARTAMENTO DE INFORMÁTICA
# 1858 - DEPARTAMENTO DE SISTEMAS DE COMPUTAÇÃO

# CURSOS DA UFPB
# cursos = cursos()
# for course in courses:
#     print(course)

# ESTUDANTES DE UM CURSO
# 1626865 - ID DO CURSO DE ENGENHARIA DA COMPUTAÇÃO
# students = students_by_course('1626865')
# students = students_by_course('1626880')
# for student in students:
# print(student)


# DISCIPLINAS DE UM CURSO
# disciplinas = classes_course("1626865", "2019", "1")
# for disciplina in disciplinas:
#     print(disciplina)

# TODOS OS ESTUDANTES DA UFPB
# all_students = 0
# for each in cursos:
#     print(f"Procurando alunos do curso {each[1]}.")
#     local = students_by_course(each[0])
#     print(f"{len(local)} alunos encontrados.")
#     all_students += len(local)

# print(f"{all_students} alunos encontrados em {len(cursos)} cursos.")
# print(f"A média de alunos por curso é {all_students/len(cursos)}")
# db = Database()

# centros = centros()
# if len(centros) != 0:
#     for centro in centros:
#         data = json.dumps(centro, ensure_ascii=False).encode('utf-8')
#         requests.post("http://localhost:8081/centers",
#                       data=data)

# dpURL = "http://localhost:8081/departments"
# departamentos = departamentos()
# if len(departamentos) != 0:
#     print(f"Sending {len(departamentos)} departme")
#     print("")
#     for dp in departamentos:
#         data = json.dumps(dp, ensure_ascii=False).encode('utf-8')
#         requests.post(dpURL, data=data)


# data = '{"id": 991991, "nome": "eae criançada"}'
# requests.post("http://localhost:8081/centers", data=data.encode('utf-8'))

# TODO - Use sets instead of lists at the scrapers returns:
# The correct way is to use db.execute(query, set) on query using %s.
# departamentos = departamentos()
# if len(departamentos) != 0:
#     for d in departamentos:
#         if d[2] == '':
#             d[2] = 0
#             db.insert(
#                 f"INSERT INTO departamentos VALUES({d[0]}, '{d[1]}', {d[2]});")

# cursos = cursos()
# if len(cursos) != 0:
#     for curso in cursos:
#         query = "INSERT INTO cursos VALUES(%s,%s,%s,%s,%s)"
# for e in cursos:
#     print(e)

# db.close()
