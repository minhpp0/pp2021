import curses
from output import outputs
from input import inputs
from domain.Student import *
from domain.Course import *
from domain.Mark import *

sc = curses.initscr()
curses.start_color()

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