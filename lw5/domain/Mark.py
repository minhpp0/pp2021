Mark = []
Mark_marks = []
Mark_gpa = []

class Marks:
    def __init__(self, cid, sid, marks, gpa=0):
        self.cid = cid
        self.sid = sid
        self.marks = marks
        self.gpa = gpa
        Mark.append(self)
        Mark_marks.append(self.marks)

    def get_cid(self):
        return self.cid

    def get_id(self):
        return self.sid

    def get_marks(self):
        return self.marks

    def get_gpa(self):
        return self.gpa

    def set_gpa(self, gpa):
        self.gpa = gpa