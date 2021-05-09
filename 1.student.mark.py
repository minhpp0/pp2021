students = []
studentID = []
courses = []
courseID = []
marks = []

def input_student():
    num = int(input("Enter the number of student in class: "))
    name = input("Enter student Name: ")
    id = input("Enter Student ID: ")
    DoB = input("Enter DoB Student: ")
    s = {'id':id,'name':name,'DoB':DoB}
    students.append(s)
    studentID.append(id)
    return num

def input_course():
    num = int(input("Enter the number of courses in class: "))
    name = input("Enter the Name of Course: ")
    id = input("Enter Course ID: ")
    c = {'id':id,'name':name}
    courses.append(c)
    courseID.append(id)
    return num

def input_mark():
    for i in range(0,len(courses)):
        cours_id = input("Enter Course ID: ")
    for j in range(0,len(students)):
        stu_id = input("Enter Student ID: ")
        mark = float(input("Enter mark of Student: "))
        m = {'S_id':stu_id,'C_id':cours_id,'mark':mark}
        marks.append(m)
        break


def list_student():
    print("List students: ")
    for i in range(0,len(students)):
        print(f"ID: {students[i]['id']}  Name: {students[i]['name']}  DoB: {students[i]['DoB']}")

def list_course():
    print("List courses")
    for i in range(0,len(courses)):
        print(f"ID: {courses[i]['id']}  Name: {courses[i]['name']}")

def list_mark():
    for i in range(0,len(marks)):
        print(f"The ID student: {marks[i]['S_id']} \nPoints: {marks[i]['mark']} ")
input_student()
input_course()
input_mark()
list_student()
list_course()
list_mark()
