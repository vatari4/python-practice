group = []
x1 = 1
countStudents = 3

for times in range(0, countStudents):
    students = input()
    group.append(students)

for main in range(0, len(group)):
    if main == len(group)-1:
        print(group[main], ' - ', group[0])
    else:
        print(group[main], ' - ', group[x1])
        x1 += 1