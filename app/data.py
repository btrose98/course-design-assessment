import random

from models import *
from faker import Faker
from faker.providers import DynamicProvider

# Create fake data to be used
fake = Faker()

courses_provider = DynamicProvider(
    provider_name="course_names",
    elements=["Computer Science", "Math", "Science", "History", "Art", "Gym", "Geography", "French"]
)
number_of_available_courses = len(courses_provider.elements)

assignments_provider = DynamicProvider(
    provider_name="assignment_names",
    elements=["assignment #1", "assignment #2", "assignment #3", "assignment #4", "assignment #5", "assignment #6", ]
)
number_of_assignments = len(assignments_provider.elements)

students = [Student(student_id, fake.name()) for student_id in range(1, 11)]
courses = [Course(course_id, fake.course_names()) for course_id in range(1, number_of_available_courses)]
assignments = [
    Assignment(
        id=assignment_id,
        name=fake.assignment_names(),
        course_id=random.randint(1, number_of_available_courses)
    ) for assignment_id in range(1, 7)
]

# Enroll each student in any number of courses
enrollments = []
for student in students:
    num_enrollments = random.randint(1, number_of_available_courses)
    for i in range(num_enrollments):
        course = random.choice(courses)
        new_enrollment = Enroll(course.id, student.id)
        enrollments.append(new_enrollment)

# Assign grades to any number of assignments


print("Students:")
for student in students:
    print(student)

print("\nCourses:")
for course in courses:
    print(course)

print("\nAssignments:")
for assignment in assignments:
    print(assignment)

print("\nEnrollments:")
for enroll in enrollments:
    print(enroll)
