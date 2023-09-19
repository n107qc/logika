class Student:
    def __init__(self, surname, name, grade):
        pass
    
        self.surname = surname
        self.name = name 
        self.grade = grade

students = []

with open('student.txt', 'r', encoding='utf-8')  as file:
    for line in file:
        data = line.split(' ')
        #print(data)
        obj = Student(data[0], data[1], int(data[2]))
        students.append(obj)

for student in students:
    if student.grade == 5:
        print(student.surname)

total_grades = sum(student.grade for student in students)
average_grade = total_grades / len(students) if students else 0

print(f'Середня оцінка: {average_grade:.2f}')
