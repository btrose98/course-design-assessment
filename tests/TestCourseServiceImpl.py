import pytest
from app.course_service_impl import CourseServiceImpl


course_service = CourseServiceImpl()
VALID_COURSE_ID = 0
INVALID_COURSE_ID = -1
TEST_COURSE_NAME = "Test Course"
ORIGINAL_COURSE_LIST = course_service.get_courses()
TEST_ASSIGNMENT_NAME = "Test Assignment"
VALID_ASSIGNMENT_ID = 0
INVALID_ASSIGNMENT_ID = -1
VALID_STUDENT_ID = 0
INVALID_STUDENT_ID = -1
VALID_STUDENT_ID_TO_ENROLL = 4
VALID_GRADE = 80
INVALID_GRADE = 110


def test_get_courses():
    courses = course_service.get_courses()
    assert len(courses) > 0

def test_get_course_by_id():
    # Course exists, valid id
    course = course_service.get_course_by_id(VALID_COURSE_ID)
    assert course.id == VALID_COURSE_ID

    # Course does not exist, invalid id
    course = course_service.get_course_by_id(INVALID_COURSE_ID)
    assert course is None

# Combine create and delete tests to avoid redundancy in creating test resources and to avoid modifying source data.
def test_create_and_delete_course():
    # Course created successfully
    new_course_id = course_service.create_course(TEST_COURSE_NAME)
    expected_course = course_service.get_course_by_id(new_course_id)
    assert expected_course.id == new_course_id

    new_course_list = course_service.get_courses()
    assert expected_course in new_course_list

    # Course deleted successfully, valid id
    course_deleted = course_service.delete_course(new_course_id)
    assert course_deleted is True

    new_course_list = course_service.get_courses()
    assert expected_course not in new_course_list

    # Failed to delete course, invalid id
    course_deleted = course_service.delete_course(INVALID_COURSE_ID)
    assert course_deleted is False

    new_course_list = course_service.get_courses()
    assert ORIGINAL_COURSE_LIST == new_course_list

def test_create_assignment():
    new_assignment_id = course_service.create_assignment(VALID_COURSE_ID, TEST_ASSIGNMENT_NAME)
    assert new_assignment_id is not None

# Combine create and delete tests to avoid redundancy in creating test resources and to avoid modifying source data.
def test_enroll_and_drop_student():
    # Successful enroll
    enrolled = course_service.enroll_student(VALID_COURSE_ID, VALID_STUDENT_ID_TO_ENROLL)
    assert enrolled is True

    # Failed enroll, student already enrolled
    enrolled = course_service.enroll_student(VALID_COURSE_ID, VALID_STUDENT_ID_TO_ENROLL)
    assert enrolled is False

    # Failed enroll, invalid course id
    enrolled = course_service.enroll_student(INVALID_COURSE_ID, VALID_STUDENT_ID_TO_ENROLL)
    assert enrolled is False

    # Failed enroll, invalid student id
    enrolled = course_service.enroll_student(VALID_COURSE_ID, INVALID_STUDENT_ID)
    assert enrolled is False

    # Successful drop
    dropped = course_service.dropout_student(VALID_COURSE_ID, VALID_STUDENT_ID_TO_ENROLL)
    assert dropped is True

    # Failed drop, invalid course id
    dropped = course_service.dropout_student(INVALID_COURSE_ID, VALID_STUDENT_ID_TO_ENROLL)
    assert dropped is False

    # Failed drop, invalid student id
    dropped = course_service.dropout_student(VALID_COURSE_ID, INVALID_STUDENT_ID)
    assert dropped is False

def test_submit_assignment():
    # Successful submit
    submitted = course_service.submit_assignment(VALID_COURSE_ID, VALID_STUDENT_ID, VALID_ASSIGNMENT_ID, VALID_GRADE)
    assert submitted is True

    # Failed submit, invalid grade
    submitted = course_service.submit_assignment(VALID_COURSE_ID, VALID_STUDENT_ID, VALID_ASSIGNMENT_ID, INVALID_GRADE)
    assert submitted is False

    # Failed submit, invalid course id
    submitted = course_service.submit_assignment(INVALID_COURSE_ID, VALID_STUDENT_ID, VALID_ASSIGNMENT_ID, VALID_GRADE)
    assert submitted is False

    # Failed submit, invalid student id
    submitted = course_service.submit_assignment(VALID_COURSE_ID, INVALID_STUDENT_ID, VALID_ASSIGNMENT_ID, VALID_GRADE)
    assert submitted is False

    # Failed submit, invalid assignment id
    submitted = course_service.submit_assignment(VALID_COURSE_ID, VALID_STUDENT_ID, INVALID_ASSIGNMENT_ID, VALID_GRADE)
    assert submitted is False

def test_get_assignment_grade_avg():
    # Successful
    avg = course_service.get_assignment_grade_avg(VALID_COURSE_ID, VALID_ASSIGNMENT_ID)
    assert avg > 0

    # Failed, invalid course id
    avg = course_service.get_assignment_grade_avg(INVALID_COURSE_ID, VALID_ASSIGNMENT_ID)
    assert avg == -1

    # Failed, invalid assignment id
    avg = course_service.get_assignment_grade_avg(VALID_COURSE_ID, INVALID_ASSIGNMENT_ID)
    assert avg == -1

def test_get_student_grade_avg():
    # Successful
    avg = course_service.get_student_grade_avg(VALID_COURSE_ID, VALID_STUDENT_ID)
    assert avg > 0

    # Failed, invalid course id
    avg = course_service.get_student_grade_avg(INVALID_COURSE_ID, VALID_STUDENT_ID)
    assert avg == -1

    # Failed, invalid student id
    avg = course_service.get_student_grade_avg(VALID_COURSE_ID, INVALID_STUDENT_ID)
    assert avg == -1

def test_get_top_five_students():
    # Successful
    top_five = course_service.get_top_five_students(VALID_COURSE_ID)
    assert len(top_five) > 0

    # Failed, invalid course id
    top_five = course_service.get_top_five_students(INVALID_COURSE_ID)
    assert len(top_five) <= 0