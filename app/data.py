import random

from app.models import *

'''
    Assumptions:
        - Deleting an instance of an object will not decrement the ids. For example, 5 students currently exist,
            resulting in ids 0-4 being assigned. If student with id=4 is deleted, then the next student id assigned
            will be 5 (not 4). Similarly, if student id=2 is deleted, the next student id assigned will be 5. In this
            case, the existing student ids would be 0,1,3-5.
'''

students = [
    Student(0, "Bradley Rose"),
    Student(1, "Celina Norman"),
    Student(2, "Ray Bray"),
    Student(3, "Joann Wang"),
    Student(4, "Antonia Perez"),
]
next_student_id = max(student.id for student in students) + 1

courses = [
    Course(0, "Computer Science"),
    Course(1, "Math"),
    Course(2, "Physics"),
    Course(3, "Music"),
    Course(4, "Gym"),
]
next_course_id = max(course.id for course in courses) + 1

assignments = [
    Assignment(0, "Assignment #1", 0),
    Assignment(1, "Assignment #2", 1),
    Assignment(2, "Assignment #3", 2),
    Assignment(3, "Assignment #4", 0),
    Assignment(4, "Assignment #5", 0),
]
next_assignment_id = max(assignment.id for assignment in assignments) + 1

enrollments = [
    Enroll(0, 0, 0),
    Enroll(1, 1, 1),
    Enroll(2, 2, 0),
    Enroll(3, 0, 2),
    Enroll(4, 0, 3),
]
next_enrollment_id = max(enrollment.id for enrollment in enrollments) + 1

grades = [
    Grade(0, 75, 0, 0),
    Grade(1, 34, 0, 2),
    Grade(2, 68, 2, 0),
    Grade(3, 100, 4, 0),
    Grade(4, 92, 3, 0),
]
next_grade_id = max(grade.id for grade in grades) + 1
