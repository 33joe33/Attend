import sqlite3

class Queries:
    def __init__(self, dataConnection=sqlite3.connect("Attendance").cursor()):
        self.dataConnection = dataConnection
    def add_class(self):
        self.dataConnection.execute("")

    def set_student_attendance(self,studentName):
        self.dataConnection.execute("INSTERT INTO ATTENDANCE ")