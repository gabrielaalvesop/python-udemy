students_grades = [
    {"nome": "Ana", "nota": 8.5},
    {"nome": "Bruno", "nota": 7.0},
    {"nome": "Carlos", "nota": 9.2}
]

def get_grade(student):
    return student["nota"]

def middle_class(students):
    return sum(get_grade(student) for student in students) / len(students)

def ranking_por_nota(students):
    return sorted(students, key=get_grade, reverse=True)

student_with_highest_grade = max(students_grades, key=get_grade)
print(f"O aluno com a maior nota é {student_with_highest_grade['nome']} "
      f"com a nota {student_with_highest_grade['nota']:.1f}.")

middle_grade = middle_class(students_grades)
print(f"A média das notas da turma é {middle_grade:.2f}.")

descending_notes = ranking_por_nota(students_grades)
print("Ranking dos alunos por nota (do maior para o menor):")
for index, student in enumerate(descending_notes, start=1):
    print(f"{index}. {student['nome']} - Nota: {student['nota']:.1f}")