from datetime import date


class Admin:
    classes = []

    def add_class(self, class_year, max_per_section):
        self.classes.append({"class_year": class_year, "sections": [], "students": set(),
                             "max_per_section": max_per_section})

    def get_class_index(self, class_year):
        for i in range(0, len(self.classes)):
            if(self.classes[i]["class_year"] == class_year ):
                class_index = i
        return class_index

    def create_new_section_name(self, class_year):

        class_index = self.get_class_index(class_year)
        if self.classes[class_index]["sections"]:
            sections = [section for section in self.classes[class_index]["sections"]]
            first_letters = []
            for i in sections:
                first_letters.append(ord(i["section_name"]))
            return chr(max(first_letters) + 1)
        else:
            return "A"

    def add_section(self, class_year, teacher="", students=set()):
        section_name = self.create_new_section_name(class_year)
        class_index = self.get_class_index(class_year)
        for c in self.classes:
            if c["class_year"] == class_year:
                self.classes[class_index]["sections"].append({"teacher": teacher, "section_name": section_name, "students": students})
        

    def add_student_to_class(self, student, class_year):
        self.classes = [c["students"].add(student) for c in self.classes if c["class_year"] == class_year]
        class_index = [i for i, c in self.classes if c["class_year"] == class_year][0]
        if filter(lambda x: len(x["students"]) <= self.classes[class_index]["max_per_section"],
                  self.classes[class_index]["sections"]):
            self.classes[class_index]["sections"] = [s["students"].add(student) for s in
                                                     self.classes[class_index]["sections"]
                                                     if
                                                     len(self.classes[class_index]["sections"]) <
                                                     self.classes[class_index]["max_per_section"]]
        else:

            self.add_section(class_year, students={student})

    def add_student_to_section(self, student, class_year, section):
        self.add_student_to_class(student, class_year)
        self.classes = [c["sections"]["students"].add(student) for c in self.classes if c["class_year"] == class_year
                        and c["sections"]["section_name"] == section]

    def add_teacher_to_section(self, class_year, section_name, teacher_id):
        class_index = [i for i, c in self.classes if c["class_year"] == class_year][0]
        section_index = [i for i, c in self.classes[class_index]["section"] if c[section_name] == section_name]
        self.classes[class_index]["section"][section_index]["teacher"] = teacher_id

    def take_attendance(self,teacher):

        for c in self.classes:
            for s in c["sections"]:
                if s["teacher"] == teacher:
                    section = s
        for stu in section["students"]:
            stu.setAttendance(date)
