students = []
studentID = []
courses = []
courseID = []
marks = []
class Student:
    def __init__(self, id, name, DoB):
        self.id = id
        self.name = name
        self.DoB = DoB

    def describe(self):
        print(self.id + " " + self.name + " " + self.DoB)
class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def describe(self):
        print(self.id + " " + self.name)
class StudentMark:
    def __init__(self, student_id, course_id, mark):
        self.student_id = student_id
        self.course_id = course_id
        self.mark = mark

    def describe(self):
        print("The ID student: " + self.student_id + " Point: " + str(self.mark))

def input_student():
    num = int(input("Enter the number of student in class: "))
    name = input("Enter student Name: ")
    id = input("Enter Student ID: ")
    DoB = input("Enter DoB Student: ")
    s = Student(id,name,DoB)
    students.append(s)
    studentID.append(id)
    return num

def input_course():
    num = int(input("Enter the number of courses in class: "))
    name = input("Enter the Name of Course: ")
    id = input("Enter Course ID: ")
    c = Course(id,name)
    courses.append(c)
    courseID.append(id)
    return num

def input_mark():
    for i in range(0,len(courses)):
        cours_id = input("Enter Course ID: ")
    for j in range(0,len(students)):
        stu_id = input("Enter Student ID: ")
        mark = float(input("Enter mark of Student: "))
        m = StudentMark(cours_id,stu_id,mark)
        marks.append(m)
        break


def list_student():
    print("List students: ")
    for i in range(0,len(students)):
        Student.describe(students[i])

def list_course():
    print("List courses")
    for i in range(0,len(courses)):
        Course.describe(students[i])

def list_mark():
    for i in range(0,len(marks)):
        StudentMark.describe(marks[i])
input_student()
input_course()
input_mark()
list_student()
list_course()
list_mark()