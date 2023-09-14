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