from app.course_service import CourseService
from typing import List, Any
from models import *
from data import *


class CourseServiceImpl(CourseService):
  """
  Please implement the CourseService interface according to the requirements.
  """

  # def __init__(self):
  #   self.courses = [
  #     Course(0, "Computer Science"),
  #     Course(1, "Finance"),
  #     Course(2, "Math")
  #   ]
  #
  #   self.assignments = [
  #     Assignment(0, "assignment 1", 0),
  #     Assignment(1, "assignment 2", 0),
  #     Assignment(2, "assignment 3", 1),
  #     Assignment(3, "assignment 4", 2)
  #   ]
  #
  #   self.students = [
  #     Student(0, "Sean"),
  #     Student(1, "Brad"),
  #     Student(2, "Mona"),
  #     Student(3, "Mikayla")
  #   ]
  #
  #   self.grades = []
  #
  #   self.next_course_id = 1
  #   self.next_assignment_id = 1
  #   self.next_student_id = 1
  #   self.next_grade_id = 1

  def get_courses(self) -> List[Any]:
    """
    Returns a list of all courses.
    """
    return self.courses

  def get_course_by_id(self, course_id) -> Any:
    """
    Returns a course by its id.
    """
    for course in self.courses:
      if course.id == course_id:
        return course
    return None

  def create_course(self, course_name) -> int:
    """
    Creates a new course.
    Returns the id of the new course.
    """
    new_course = Course(self.next_course_id, course_name)
    self.next_course_id += 1
    self.courses.append(new_course)
    return new_course.id

  def delete_course(self, course_id) -> bool:
    """
    Deletes a course by its id.
    Returns True if the course was deleted successfully, otherwise False.
    """
    course = self.get_course_by_id(course_id)
    if course is None:
      return False

    self.courses.remove(course)

    return True

  def create_assignment(self, course_id, assignment_name) -> int:
    """
    Creates a new assignment for a course.
    Returns the id of the new assignment.
    """
    new_assignment = Assignment(self.next_assignment_id, assignment_name, course_id)
    self.next_assignment_id += 1
    self.assignments.append(new_assignment)
    return new_assignment.id

  def enroll_student(self, course_id, student_id) -> bool:
    """
    Enrolls a student in a course.
    Returns True if the student was enrolled successfully, otherwise False.
    """
    pass

  def dropout_student(self, course_id, student_id) -> bool:
    """
    Drops a student from a course.
    Returns True if the student was dropped successfully, otherwise False.
    """
    pass

  def submit_assignment(self, course_id, student_id, assignment_id, grade: int) -> bool:
    """
    Submits an assignment for a student. A grade of an assignment will be an integer between 0 and 100 inclusive.
    Returns True if the assignment was submitted successfully, otherwise False.
    """
    if not 0 <= grade <= 100:
      return False

    submission = Grade(self.next_grade_id, grade, assignment_id, student_id)
    self.next_grade_id += 1
    self.grades.append(submission)
    return True

  # This tells me that Submission/Grade should have FKs to Course and Assignment.
  def get_assignment_grade_avg(self, course_id, assignment_id) -> int:
    """
    Returns the average grade for an assignment. Floors the result to the nearest integer.
    """
    assignment = self._get_assignment_by_id(assignment_id)
    if assignment is None:
      return -1

    grades = self._get_grades_by_assignment_id(assignment_id)
    avg = sum(grades) / len(grades)
    return avg.__floor__()

  def get_student_grade_avg(self, course_id, student_id) -> int:
    """
    Returns the average grade for a student in a course. Floors the result to the nearest integer.
    """
    student_grades = []
    assignments = self._get_assignments_by_course_id(course_id)
    for assignment in assignments:
      grades = self._get_grades_by_assignment_id(assignment.id)
      for grade in grades:
        if grade.student_id == student_id:
          student_grades.append(grade)

    # grades = self._get_grades_by_student_id(student_id)
    avg = sum(student_grades) / len(student_grades)
    return avg.__floor__()

  def get_top_five_students(self, course_id) -> List[int]:
    """
    Returns the IDs of the top 5 students in a course based on their average grades of all assignments.
    """
    course_student_grades = []
    for student in self.students:
      avg = self.get_student_grade_avg(course_id, student.id)
      obj = {
        'student_id': student.id,
        'avg': avg
      }

      course_student_grades.append(obj)

      sorted_obj_list = sorted(course_student_grades, key=lambda x: x['avg'], reverse=True)

      top_five = sorted_obj_list[:5]

      top_5_student_ids = [entry['student_id'] for entry in top_five]

      return top_5_student_ids

  def _get_assignments_by_course_id(self, course_id):
    assignments = []
    for assignment in assignments:
      if assignment.course_id == course_id:
        assignments.append(assignment)

    return assignments

  def _get_grades_by_student_id(self, student_id):
    student_grades = []
    for grade in self.grades:
      if grade.student_id == student_id:
        student_grades.append(grade)

    return student_grades

  def _get_grades_by_assignment_id(self, assignment_id):
    assignment_grades = []
    for grade in self.grades:
      if grade.assignment_id == assignment_id:
        assignment_grades.append(grade)

    return assignment_grades

  def _get_assignment_by_id(self, assignment_id):
    for assignment in self.assignments:
      if assignment.id == assignment_id:
        return assignment
    return None