students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])
    
students.sort(key=lambda x: x[1])

second_lowest_grade = sorted(list(set([x[1] for x in students])))[1]

second_lowest_students = [s[0] for s in students if s[1] == second_lowest_grade]

second_lowest_students.sort()

for student in second_lowest_students:
    print(student)
    
