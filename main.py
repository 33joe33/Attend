#import student
import Admin
import sqlite3
#s= student.Student("joe")
#s.setAttendance()
#s.getAttendance("Week")

admin = Admin.Admin()

admin.add_class(1,20)
admin.add_section(1, "Mr Jones")
admin.add_section(1, "Mr smith")
admin.add_section(1, "dasdfasd")
admin.add_student_to_class(1)
print(admin.classes)