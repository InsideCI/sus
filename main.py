from disciplinas_departamento import *
from cursos_ufpb import *
from alunos_curso import *

import request_alunos_curso as rac

# classes_and_teachers_dep('G', '2151', '2019', '1')
# classes_and_teachers_dep('G', '1858', '2019', '1')
# classes_and_teachers_dep('G', '1859', '2019', '1')

# 1859 - DEPARTAMENTO DE COMPUTAÇÃO CIENTÍFICA
# 2151 - DEPARTAMENTO DE INFORMÁTICA
# 1858 - DEPARTAMENTO DE SISTEMAS DE COMPUTAÇÃO

courses = ufpb_courses()
# for each in courses:
#     print(each)

# 1626865 - ID DO CURSO DE ENGENHARIA DA COMPUTAÇÃO
# students = students_by_course('1626865')
# for student in students:
#     print(student)

# students = rac.students_by_course('1626865')
# for student in students:
#     print(student)


all_students = list()
for each in courses:
    print(f"Procurando alunos do curso {each[1]}.")
    local = rac.students_by_course(each[0])
    print(f"{len(local)} alunos encontrados.")
    all_students += local

print(f"{len(all_students)} alunos encontrados em {len(courses)} cursos.")
print(f"A média de alunos por curso é {len(all_students)/len(courses)}")
