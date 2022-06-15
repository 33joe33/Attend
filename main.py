#import student
import Admin
from tkinter import *
from tkinter.ttk import *
from functools import partial

# import sqlite3

window = Tk()

login_frame = Frame(window)
add_section_frame = Frame(window)
user_frame = Frame(window)

s = student.Student("joe")
s.setAttendance()
s.getAttendance("Week")

admin = Admin.Admin()

admin.add_class(1,20)
admin.add_section(1, "Mr Jones")
admin.add_section(1, "Mr smith")
admin.add_section(1, "dasdfasd")
admin.add_student_to_class(s, 1)


def validate_login(username, password, but):
    if username.get() == "admin" and password.get() == "password":
        but.master.destroy()
        admin_frame = create_admin_frame()
        admin_frame.pack()
    elif username.get() == "user" and password.get() == "password":
        login_frame.destroy()
        user_frame.pack()


def add_class_btn_click(but):
    but.master.destroy()
    add_class_frame = create_add_class_frame()
    add_class_frame.pack()


def add_class(class_year, max_students_per_section,but):
    but.master.destroy()
    admin.add_class(class_year.get(), max_students_per_section.get())
    add_class_frame.destroy()
    admin_frame = create_admin_frame()
    admin_frame.pack()


def display_insert(stud, time):
    display.delete(*display.get_children())
    for e in stud.getAttendance(time):
        for entry in e:
            display.insert(parent='', index='end', text='', values=entry)


def validate_user(student):
    studentobj, student_class, student_section = admin.find_student(student.get())
    user_frame.destroy()
    button_frame = Frame(display_frame)
    display_insert_week =partial(display_insert,studentobj,"Week")
    display_insert_month =partial(display_insert,studentobj,"Week")
    display_insert_year =partial(display_insert,studentobj,"Week")

    Button(button_frame, text="Week", command=display_insert_week).pack()
    Button(button_frame, text="Month", command=display_insert_month).pack()
    Button(button_frame, text="Year", command=display_insert_year).pack()
    #display.delete()
    display_header.pack()
    button_frame.pack()
    display.pack()
    Label(display_header, text="  Student name: " + studentobj.Name + "     Class: " + str(
        student_class) + "     Section: " + student_section).pack()

    display_frame.pack()


def add_section(class_year, teacher_name, student_name):
    s = student.Student(student_name.get())
    admin.add_section(class_year.get(), teacher_name.get(), {s})


def create_add_section_frame():
    add_section_frame = Frame(window)
    Label(add_section_frame, text="Please enter the class year").grid(row=0, column=0)
    class_year = IntVar()
    Entry(add_section_frame, textvariable=class_year).grid(row=1, column=0)
    Label(add_section_frame, text="Please enter the teacher's name").grid(row=2, column=0)
    teacher_name = StringVar()
    Entry(add_section_frame, textvariable=teacher_name).grid(row=3, column=0)
    Label(add_section_frame, text="Please enter the name of the student").grid(row=4, column=0)
    student_name = StringVar()
    Entry(add_section_frame, textvariable=student_name).grid(row=5, column=0)
    addSection = partial(add_section, class_year, teacher_name, student_name)
    Button(add_section_frame, text="submit", command=addSection).grid(row=6, column=0)
    but=Button(add_section_frame, text="back", command=lambda:add_class_back(but))
    but.grid(row=7, column=0)
    return add_section_frame


def add_student_to_class(student_name,class_year):
    admin.add_student_to_class(student.Student(student_name.get()),class_year.get())

def add_student_to_section(student_name, class_year, section_name):
    admin.add_student_to_section(student.Student(student_name.get()),class_year.get(),section_name.get())

def create_add_student_frame():
    add_student_frame = Frame(window)
    Label(add_student_frame, text="Please enter the class year").grid(row=0, column=0)
    class_year = IntVar()
    Entry(add_student_frame, textvariable=class_year).grid(row=1, column=0)
    Label(add_student_frame, text="Please enter the student's name").grid(row=2, column=0)
    student_name = StringVar()
    Entry(add_student_frame, textvariable=student_name).grid(row=3, column=0)
    Label(add_student_frame, text="Please enter the name of the section").grid(row=4, column=0)
    section_name = StringVar()
    Entry(add_student_frame, textvariable=section_name).grid(row=5, column=0)
    addStudentToClass = partial(add_student_to_class, student_name, class_year)
    addStudentToSection = partial(add_student_to_section,student_name,class_year,section_name)
    Button(add_student_frame, text="add student to class", command=addStudentToClass).grid(row=6, column=0)
    Button(add_student_frame, text="add student to section", command=addStudentToSection).grid(row=6, column=1)
    but=Button(add_student_frame, text="back", command=lambda:add_class_back(but))
    but.grid(row=7, column=0)
    return add_student_frame


def add_teacher_to_section(class_year,section_name,teacher_id):
    admin.add_teacher_to_section(class_year.get(), section_name.get(),teacher_id.get())


def create_add_teacher_frame():
    add_teacher_frame = Frame(window)
    Label(add_teacher_frame, text="Please enter the class year").grid(row=0, column=0)
    class_year = IntVar()
    Entry(add_teacher_frame, textvariable=class_year).grid(row=1, column=0)
    Label(add_teacher_frame, text="Please enter the name of the section").grid(row=4, column=0)
    section_name = StringVar()
    Entry(add_teacher_frame, textvariable=section_name).grid(row=5, column=0)
    Label(add_teacher_frame, text="Please enter the name of the teacher").grid(row=4, column=0)
    teacher_name = StringVar()
    Entry(add_teacher_frame, textvariable=section_name).grid(row=5, column=0)
    addTeacherToSection = partial(add_teacher_to_section,class_year, section_name,teacher_name)
    Button(add_teacher_frame, text="submit", command=addTeacherToSection).grid(row=6, column=0)
    but=Button(add_teacher_frame, text="back", command=lambda:add_class_back(but))
    but.grid(row=7, column=0)
    return add_teacher_frame

def add_section_btn_click(but):
    but.master.destroy()
    add_section_frame = create_add_section_frame()
    add_section_frame.pack()

def add_student_to_btn_click(but):
    but.master.destroy()
    global add_student_frame
    add_student_frame= create_add_student_frame()
    add_student_frame.pack()

def add_teacher_btn_click(but):
    but.master.destroy()
    add_teacher_frame = create_add_teacher_frame()
    add_teacher_frame.pack()


def create_admin_frame():
    admin_frame = Frame(window)
    Label(admin_frame, text="Welcome to admin").grid(row=0, column=0)
    but =Button(admin_frame, text="Add a class", command=lambda:add_class_btn_click(but))
    but.grid(row=1, column=0)
    but2 =Button(admin_frame, text="Add a section", command=lambda :add_section_btn_click(but2))
    but2.grid(row=1, column=1)
    but3=Button(admin_frame, text="Add student to a class/section",command=lambda:add_student_to_btn_click(but3))
    but3.grid(row=2, column=0)
    but4 =Button(admin_frame, text="Add teacher to a section",command=lambda:add_teacher_btn_click(but4))
    but4.grid(row=2, column=1)
    but5 =Button(admin_frame, text="back to login",command=lambda:admin_back(but5))
    but5.grid(row=3, column=0)
    return admin_frame


def create_add_class_frame():
    add_class_frame = Frame(window)
    Label(add_class_frame, text="Please enter the class year").grid(row=0, column=0)
    class_year = IntVar()
    Entry(add_class_frame, textvariable=class_year).grid(row=1, column=0)
    Label(add_class_frame, text="Please Enter maximum students per section").grid(
        row=2, column=0)
    max_students_per_section = IntVar()
    Entry(add_class_frame, textvariable=max_students_per_section).grid(row=3, column=0)
    addClass = partial(add_class, class_year, max_students_per_section)
    but1=Button(add_class_frame, text="submit", command=lambda:addClass(but1))
    but1.grid(row=4, column=0)
    but=Button(add_class_frame, text="back", command=lambda:add_class_back(but))
    but.grid(row=5, column=0)
    return add_class_frame


def add_class_back(but):
    but.master.destroy()
    admin_frame = create_admin_frame()
    admin_frame.pack()


def admin_back(but):
    but.master.destroy()
    login_frame = create_login_frame()
    login_frame.pack()

def create_login_frame():
    login_frame = Frame(window)
    Label(login_frame, text="User Name").grid(row=0, column=0)
    username = StringVar()
    Entry(login_frame, textvariable=username).grid(row=0, column=1)
    Label(login_frame, text="Password").grid(row=1, column=0)
    password = StringVar()
    Entry(login_frame, textvariable=password, show='*').grid(row=1, column=1)
    validateLogin = partial(validate_login, username, password)
    but =Button(login_frame, text="Login", command=lambda:validateLogin(but))
    but.grid(row=4, column=0)
    return login_frame

Label(user_frame, text="enter student name").pack()
student_e = StringVar()
student_name_entry = Entry(user_frame, textvariable=student_e)
student_name_entry.pack()
validate_user = partial(validate_user, student)
student_name_btn = Button(user_frame, text="Enter", command=validate_user)
student_name_btn.pack()
display_frame = Frame(window)
display_header = Frame(display_frame)
display = Treeview(display_frame)

display['columns'] = ('date', 'present')
display.column("date", anchor=CENTER, width=80)
display.column("present", anchor=CENTER, width=80)
display.heading("date", text="date", anchor=CENTER)
display.heading("present", text="present", anchor=CENTER)

login_frame = create_login_frame()
login_frame.pack()
admin_frame = create_admin_frame()
add_class_frame = create_add_class_frame()
add_section_frame = create_add_section_frame()
add_student_frame = create_add_student_frame()
add_teacher_frame = create_add_teacher_frame()




window.mainloop()
