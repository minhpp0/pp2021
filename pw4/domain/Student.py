Students = []
StudentID = []

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
