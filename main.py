from disciplinas_departamento import *
from disciplinas_curso import *
from cursos_ufpb import *
from alunos_curso import *

# classes_and_teachers_dep('G', '2151', '2019', '1')
# classes_and_teachers_dep('G', '1858', '2019', '1')
# classes_and_teachers_dep('G', '1859', '2019', '1')

# 1859 - DEPARTAMENTO DE COMPUTAÇÃO CIENTÍFICA
# 2151 - DEPARTAMENTO DE INFORMÁTICA
# 1858 - DEPARTAMENTO DE SISTEMAS DE COMPUTAÇÃO

# CURSOS DA UFPB
# courses = ufpb_courses()
# for course in courses:
#     print(course)

# ESTUDANTES DE UM CURSO
# 1626865 - ID DO CURSO DE ENGENHARIA DA COMPUTAÇÃO
# students = students_by_course('1626865')
students = students_by_course('1626880')
for student in students:
    print(student)


# DISCIPLINAS DE UM CURSO
# disciplinas = classes_course("1626865", "2019", "1")
# for disciplina in disciplinas:
#     print(disciplina)

# TODOS OS ESTUDANTES DA UFPB
# all_students = 0
# for each in courses:
#     print(f"Procurando alunos do curso {each[1]}.")
#     local = students_by_course(each[0])
#     print(f"{len(local)} alunos encontrados.")
#     all_students += len(local)

# print(f"{all_students} alunos encontrados em {len(courses)} cursos.")
# print(f"A média de alunos por curso é {all_students/len(courses)}")