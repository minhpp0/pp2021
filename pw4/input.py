import math
import numpy as np
import curses
from domain.Student import *
from domain.Course import *
from domain.Mark import *

sc = curses.initscr()
curses.start_color()
class input():

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