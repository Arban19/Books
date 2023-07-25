students = {
    "Hermoine": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
# print(students["Hermoine"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])


for student in students:
    print(student)

for student in students:
    print(student, students[student], sep=", ")