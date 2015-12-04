student = {"labmeret": 45, "nev": "Tibike", "kor": 8.5}
print(student)

print(student["labmeret"])


students = [
{"name": "tibi", "age": 6},
{"name": "adorjan", "age": 9},
{"name": "bela", "age": 6},
{"name": "aurel", "age": 12},
{"name": "dezso", "age": 4},
]


def students_at_leat_8(list):
    output= []
    for char in list:
        if char <= 9:
            output.append(list["name"])
    return output

students = students_at_leat_8(students)
print(output)
