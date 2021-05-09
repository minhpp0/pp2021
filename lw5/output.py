import numpy as np
import curses
from domain.Student import *
from domain.Course import *
from domain.Mark import *

sc = curses.initscr()
curses.start_color()

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