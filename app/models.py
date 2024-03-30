class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"{self.id}: {self.name}"


class Student:
    def __init__(self, id, name):
        self.id = id,
        self.name = name

    def __repr__(self):
        return f"{self.id}: {self.name})"


class Assignment:
    def __init__(self, id, name, course_id):
        self.id = id
        self.name = name
        self.course_id = course_id

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.course_id})"


class Grade:
    def __init__(self, id, score, assignment_id, student_id):
        self.id = id
        self.score = score
        self.assignment_id = assignment_id
        self.student_id = student_id

    def __repr__(self):
        return f"Assignment: {self.assignment_id}, Student: {self.student_id}, Score: {self.score}"


class Enroll:
    def __init__(self, course_id, student_id):
        self.course_id = course_id
        self.student_id = student_id

    def __repr__(self):
        return f"Student: {self.student_id} enrolled in Course: {self.course_id}"
