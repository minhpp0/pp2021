import math
import numpy as np
import curses

Students = []
StudentID = []
Courses = []
CoursesID = []
Courses_credit = []
Mark = []
Mark_marks = []
Mark_gpa = []

sc = curses.initscr()
curses.start_color()

class Student:
    def __init__(self, id, doB, name):
        self.name = name
        self.id = id
        self.dob = doB
        Students.append(self)
        StudentID.append(self.id)

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_dob(self):
        return self.dob

class Course:
    def __init__(self, cid, name, credit):
        self.cid = cid
        self.name = name
        self.credit = credit
        Courses.append(self)
        CoursesID.append(self.cid)
        Courses_credit.append(self.credit)

    def get_cid(self):
        return self.cid

    def get_name(self):
        return self.name

    def get_credit(self):
        return self.credit

class Marks:
    def __init__(self, cid, sid, marks, gpa=0):
        self.cid = cid
        self.sid = sid
        self.marks = marks
        self.gpa = gpa
        Mark.append(self)
        Mark_marks.append(self.marks)

    def get_cid(self):
        return self.cid

    def get_id(self):
        return self.sid

    def get_marks(self):
        return self.marks

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa

class main:
 print("")
def input_number_student():
        while True:
            sc.refresh()
            Num_student = int(sc.getstr().decode())
            curses.init_pair(1, curses.A_BOLD, curses.A_UNDERLINE)
            sc.addstr("Invalid number\n", curses.color_pair(1))
            sc.refresh()
            curses.napms(3000)
            sc.clear()
            sc.refresh()

            return Num_student

def input_number_course():
        while True:
            sc.refresh()
            Num_course = int(sc.getstr().decode())
            curses.init_pair(1, curses.A_BOLD, curses.A_UNDERLINE)
            sc.addstr("Invalid number\n", curses.color_pair(1))
            sc.refresh()
            curses.napms(3000)
            sc.clear()
            sc.refresh()

            return Num_course

def inputstudent():
        sc.addstr("Enter StudentID:")
        sc.refresh()
        id = sc.getstr().decode()

        sc.addstr("Enter StudentName:")
        sc.refresh()
        name = sc.getstr().decode()

        sc.addstr("Enter date of brith:")
        sc.refresh()
        dob = sc.getstr().decode()
        Student(id, name, dob)

def inputCourses():
        sc.addstr("Enter CourseID:")
        sc.refresh()
        cid = sc.getstr().decode()

        sc.addstr("Enter CourseName:")
        sc.refresh()
        name = sc.getstr().decode()

        sc.addstr("Enter CourseCredit:")
        sc.refresh()
        credit = float(sc.getstr().decode())
        Course(cid, name, credit)

def inputmark():
        sc.addstr("- Enter the courseID you want to input mark: ")
        cid = (sc.getstr().decode())
        sc.clear()
        sc.refresh()
        if cid in CoursesID:
            sc.addstr("- Enter the StudentID you want to input mark: ")
            id = sc.getstr().decode()
            sc.clear()
            sc.refresh()
            if id in StudentID:
                while True:
                    sc.addstr(" input mark of this student in courses: ")
                    marks = math.floor(float(sc.getstr().decode()))
                    if marks < 0 or marks > 10:
                        curses.init_pair(1, curses.A_BOLD, curses.A_UNDERLINE)
                        sc.addstr("Invalid number!\n", curses.color_pair(1))
                        sc.refresh()
                        curses.napms(500)
                        sc.clear()
                        sc.refresh()
                        sc.addstr("Press enter number: ")
                        marks = math.floor(float(sc.getstr().decode()))
                    else:
                        break
            else:
                exit()
        else:
            exit()

        Marks(cid, id, marks)

def Gpa():

        value = np.array([Mark_marks])
        cre = np.array([Courses_credit])
        sc.addstr("GpA of student:")
        id = sc.getstr().decode()
        if id in StudentID:
            for i in range(0, len(Students)):
                totalCredit = np.sum(cre)
                totalValue = np.sum(np.multiply(value, cre))
                sc.refresh()
                gpa = totalValue / totalCredit
                sc.refresh()
        else:
            return 0

        Mark_gpa.append(gpa)
        sc.refresh()
        for mark in Mark:
            sc.clear()
            sc.refresh()
            sc.addstr(" [Mark_studentID: ] %s   [Gpa: ]%s \n" % (mark.get_id(), gpa))
            sc.refresh()

            break


def ShowStudent():
    sc.addstr("Lists of student:\n")
    sc.refresh()
    for student in Students:
        sc.addstr("[StudentID: ] %s    [StudentName: ] %s     [StudentDOB: ] %s \n" % (
            student.get_id(), student.get_name(), student.get_dob()))
        sc.refresh()

def ShowCourses():
        sc.addstr("Lists of Courses:\n")
        sc.refresh()
        for course in Courses:
            sc.addstr("[CourseID: ] %s     [CourseName: ] %s     [CourseCredits: ] %s\n" % (
            course.get_cid(), course.get_name(), course.get_credit()))
            sc.refresh()

def ShowMarks():
        sc.addstr("Show lists of mark:\n")
        sc.refresh()
        for mark in Mark:
            sc.addstr("[Mark_courses_id: ] %s     [Mark_student_id: ] %s    [Mark_mark: ] %s\n" % (
            mark.get_cid(), mark.get_id(), mark.get_marks()))
            sc.refresh()

def GPA_decending():
        arr = np.array([Mark_gpa])
        arr[::-1].sort()
        sc.addstr("The list after sorting is %s: \n" % (arr))
        sc.refresh()


def main():
    sc.refresh()
    sc.clear()
    try:
        sc.addstr(0, 5, "Input student and courses ?")
        sc.addstr(1, 5, " Yes")
        sc.addstr(2, 5, " No \n")
    except curses.error:
        pass
    option1 = int(sc.getstr().decode())
    while True:
        if option1 == 1:
            sc.clear()
            N_co = int(input_number_course())
            sc.clear()
            sc.refresh()
            for i in range(N_co):
                sc.addstr(f"Course {i + 1} \n")
                inputCourses()
                sc.refresh()
                N_st = int(input_number_student())
                sc.refresh()
                sc.clear()
                for i in range(N_st):
                    sc.addstr(f"Student {i + 1} \n")
                    inputstudent()
                    sc.refresh()
                    sc.clear()
                    inputmark()
                    sc.clear()
                    sc.refresh()
            break
        else:
            sc.addstr("say goodbye!!")
            curses.napms(2000)
            curses.endwin()
            exit()

    sc.refresh()
    sc.clear()
    try:
        sc.addstr(0, 5, "Calculater GPA of student ?")
        sc.addstr(1, 5, " Yes")
        sc.addstr(2, 5, " No \n")
    except curses.error:
        pass
    option2 = int(sc.getstr().decode())
    if option2 == 1:
        sc.refresh()
        Gpa()
        curses.napms(2000)
        sc.clear()
        sc.refresh()
    else:
        sc.addstr("say goodbye!!")
        curses.napms(2000)
        curses.endwin()

    while True:
        sc.addstr("1. Display list of Students: \n")
        sc.addstr("2. Display list of Courses: \n")
        sc.addstr("3. Display marks \n")
        sc.addstr("4. GPA_descending \n")
        sc.addstr("5. Stop \n")
        option3 = int(sc.getstr().decode())
        sc.refresh()
        sc.clear()
        sc.refresh()
        if option3 == 1:
            ShowStudent()
        if option3 == 2:
            ShowCourses()
        if option3 == 3:
            ShowMarks()
        if option3 == 4:
            GPA_decending()
        elif option3 == 5:
            sc.addstr("  Finish!!\n  ")
            sc.refresh()
            curses.napms(1000)
            curses.endwin()
            exit()


if __name__ == '__main__':
    main()