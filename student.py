import os

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

    def setAttendance(self, d=date.today()):
        self.Attendance[d] = self.present()

    def getAttendance(self, WeekMonthYear, d=date.today()):
        record = []
        try:
            if WeekMonthYear == "Year":
                year = d.year
                while d.year == year:
                    print(d, self.Attendance[d])
                    record.append([d, self.Attendance[d]])
                    d = passTime(d)

            if WeekMonthYear == "Month":
                month = d.month
                while d.month == month:
                    print(d, self.Attendance[d])
                    record.append([d, self.Attendance[d]])
                    d = passTime(d)
            if WeekMonthYear== "Week":
                while d.weekday() !=6:
                    record.append([d, self.Attendance[d]])
                    d = self.passTime(d)
        except KeyError:
            print("record out of range")