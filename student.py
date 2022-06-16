import os
import sqlite3

from datetime import date, timedelta


def passTime(d):
    if d.weekday() > 4:
        d -= timedelta(2)
    return d - timedelta(1)


class Student:
    def __init__(self, Name):
        self.Name = Name

    Attendance = {}

    def present(self):
        pres = input("Is " + self.Name + " present? y/n")
        if pres == "y":
            return 1
        if pres == "n":
            return 0
        print("Invalid input")
        return self.present()

    def setAttendance(self,present, d=date.today()):
        #present = self.present()
        database("INSERT INTO ATTENDANCE (STUDENT_NAME, DATE,MONTH,YEAR, PRESENT) VALUES (?, ? ,?,?,?)",
                 (self.Name, date.today(), date.today().month, date.today().year, present))

    def get_Month(self, Month):
        con = sqlite3.connect("Attendance.db")
        cur = con.cursor()
        cur.execute("SELECT DATE, PRESENT FROM ATTENDANCE WHERE MONTH IS ? AND STUDENT_NAME IS ? ",
                    (str(Month), self.Name))
        return cur.fetchall()
        con.close()
    def get_Year(self, Year):
        con = sqlite3.connect("Attendance.db")
        cur = con.cursor()
        cur.execute("SELECT DATE, PRESENT FROM ATTENDANCE WHERE YEAR IS ? AND STUDENT_NAME IS ? ", (str(Year), self.Name))
        return cur.fetchall()
        con.close()

    def getAttendance(self, WeekMonthYear, d=date.today()):
        record = []
        try:
            if WeekMonthYear == "Year":
                record.append(self.get_Year(date.today().year))

            if WeekMonthYear == "Month":

                numberOfMonths = input("Number of months")
                m = date.today().month
                for i in range(int(numberOfMonths)):
                    record.append(self.get_Month(m))

                    m = (m - 1) * (m != 0) + 12 * (m == 0)
                return record
            if WeekMonthYear == "Week":
                while d.weekday() != 6:
                    con = sqlite3.connect("Attendance.db")
                    cur = con.cursor()
                    cur.execute("SELECT DATE, PRESENT FROM ATTENDANCE WHERE  DATE IS ? AND STUDENT_NAME IS ? ",
                                (d, self.Name))
                    record.append( cur.fetchall())
                    con.close()
                    d = passTime(d)
                return record
        except KeyError:
            print("record out of range")


def database(exe, values):
    con = sqlite3.connect("Attendance.db")
    cur = con.cursor()
    cur.execute(exe, values)
    con.commit()
    con.close()
