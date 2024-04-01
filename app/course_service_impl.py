from app.course_service import CourseService
from typing import List, Any
from app.data import *


class CourseServiceImpl(CourseService):
    """
  Please implement the CourseService interface according to the requirements.
  """

    def get_courses(self) -> List[Any]:
        """
    Returns a list of all courses.
    """
        return courses

    def get_course_by_id(self, course_id) -> Any:
        """
    Returns a course by its id.
    """
        for course in courses:
            if course.id == course_id:
                return course
        print(f"Course: {course_id} does not exist")
        return None

    def create_course(self, course_name) -> int:
        """
    Creates a new course.
    Returns the id of the new course.
    """
        new_course = Course(next_course_id, course_name)
        self._increment_next_id_pointer(next_course_id)
        courses.append(new_course)
        return new_course.id

    def delete_course(self, course_id) -> bool:
        """
    Deletes a course by its id.
    Returns True if the course was deleted successfully, otherwise False.
    """
        course = self.get_course_by_id(course_id)
        if course is None:
            return False

        courses.remove(course)

        return True

    def create_assignment(self, course_id, assignment_name) -> int:
        """
    Creates a new assignment for a course.
    Returns the id of the new assignment.
    """
        new_assignment = Assignment(next_assignment_id, assignment_name, course_id)
        self._increment_next_id_pointer(next_assignment_id)
        assignments.append(new_assignment)
        return new_assignment.id

    def enroll_student(self, course_id, student_id) -> bool:
        """
    Enrolls a student in a course.
    Returns True if the student was enrolled successfully, otherwise False.
    """
        course = self.get_course_by_id(course_id)
        if course is None:
            print("\nEnroll Failed.")
            return False  # Course doesn't exist

        student = self._get_student_by_id(student_id)
        if student is None:
            print(f"\nEnroll Failed.")
            return False  # Student doesn't exist

        enrolled = self._is_student_enrolled(course_id, student_id)
        if enrolled:
            print(f"Student: {student_id} is already enrolled in Course: {course_id}. \nEnroll Failed.")
            return False  # Already enrolled

        new_enrollment = Enroll(next_enrollment_id, course_id, student_id)
        self._increment_next_id_pointer(next_enrollment_id)
        enrollments.append(new_enrollment)
        print(f"Student: {student_id} successfully enrolled in Course: {course_id}")
        return True

    def dropout_student(self, course_id, student_id) -> bool:
        """
    Drops a student from a course.
    Returns True if the student was dropped successfully, otherwise False.
    """
        if self.get_course_by_id(course_id) is None:
            print("\ndrop student failed.")
            return False  # Course doesn't exist

        if self._get_student_by_id(student_id) is None:
            print("\ndrop student failed.")
            return False  # Student doesn't exist

        for enrollment in enrollments:
            if enrollment.course_id == course_id and enrollment.student_id == student_id:
                enrollments.remove(enrollment)
                print(f"Student: {student_id} successfully dropped Course: {course_id}")
                return True
        print(f"Student: {student_id} is not currently enrolled in Course: {course_id}.\ndrop student failed.")
        return False

    def submit_assignment(self, course_id, student_id, assignment_id, grade: int) -> bool:
        """
    Submits an assignment for a student. A grade of an assignment will be an integer between 0 and 100 inclusive.
    Returns True if the assignment was submitted successfully, otherwise False.
    """

        if not 0 <= grade <= 100:
            print(f"Invalid grade.\nFailed to submit assignment: {assignment_id}.")
            return False

        if self.get_course_by_id(course_id) is None:
            print(f"\nFailed to submit assignment: {assignment_id}.")
            return False  # Course doesn't exist

        if self._get_student_by_id(student_id) is None:
            print(f"\nFailed to submit assignment: {assignment_id}.")
            return False  # Student doesn't exist

        if self._get_assignment_by_id(assignment_id) is None:
            print(f"\nFailed to submit assignment: {assignment_id}.")
            return False  # Assignment does not exist

        submission = Grade(next_grade_id, grade, assignment_id, student_id)
        self._increment_next_id_pointer(next_grade_id)
        grades.append(submission)
        return True

    def get_assignment_grade_avg(self, course_id, assignment_id) -> int:
        """
    Returns the average grade for an assignment. Floors the result to the nearest integer.
    """
        course = self.get_course_by_id(course_id)
        if course is None:
           return -1

        assignment = self._get_assignment_by_id(assignment_id)
        if assignment is None:
            print(f"\nInvalid average grade for assignment: {assignment_id}")
            return -1

        grades = self._get_grades_by_assignment_id(assignment_id)
        avg = sum(grade.score for grade in grades) / len(grades)
        return avg.__floor__()

    def get_student_grade_avg(self, course_id, student_id) -> int:
        """
    Returns the average grade for a student in a course. Floors the result to the nearest integer.
    """

        student = self._get_student_by_id(student_id)
        course = self.get_course_by_id(course_id)
        if (student or course) is None:
            print("\nUnable to get student average.")
            return -1

        course_assignments = self._get_assignments_by_course_id(course_id)

        student_grades = []

        for assignment in course_assignments:
            assignment_grades = self._get_grades_by_assignment_id(assignment.id)
            for grade in assignment_grades:
                if grade.student_id == student_id:
                    student_grades.append(grade.score)

        if not student_grades:
            print(f"Student: {student_id} has no grades in Course: {course_id}")
            return -1

        print(f"student_grades: {student_grades}")
        avg = sum(student_grade for student_grade in student_grades) / len(student_grades)
        return avg.__floor__()

    def get_top_five_students(self, course_id) -> List[int]:
        """
    Returns the IDs of the top 5 students in a course based on their average grades of all assignments.
    """
        course = self.get_course_by_id(course_id)
        if course is None:
            return []

        course_student_grades = []
        for student in students:
            avg = self.get_student_grade_avg(course_id, student.id)
            student_details = {
                'id': student.id,
                'avg': avg
            }

            course_student_grades.append(student_details)

            sorted_obj_list = sorted(course_student_grades, key=lambda x: x['avg'], reverse=True)

            top_five = sorted_obj_list[:5]

            top_5_student_ids = [entry['id'] for entry in top_five]

            return top_5_student_ids




    def _get_assignments_by_course_id(self, course_id):
        course_assignments = [assignment for assignment in assignments if assignment.course_id == course_id]
        return course_assignments

    def _get_grades_by_student_id(self, student_id):
        student_grades = [grade for grade in grades if grade.student_id == student_id]
        return student_grades

    def _get_grades_by_assignment_id(self, assignment_id):
        assignment_grades = [grade for grade in grades if grade.assignment_id == assignment_id]
        return assignment_grades

    def _get_assignment_by_id(self, assignment_id):
        for assignment in assignments:
            if assignment.id == assignment_id:
                return assignment
        print(f"Assignment: {assignment_id} does not exist.")
        return None

    def _increment_next_id_pointer(self, pointer):
        # Assumption - will never decrement when object is deleted from system
        pointer += 1

    def _is_student_enrolled(self, course_id, student_id):
        for enroll in enrollments:
            if enroll.course_id == course_id and enroll.student_id == student_id:
                return True
        return False

    def _get_student_by_id(self, student_id):
        for student in students:
            if student.id == student_id:
                return student
        print(f"Student: {student_id} does not exist.")
        return None
