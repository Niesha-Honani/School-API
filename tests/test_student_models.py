'''
Docstring for school-api 1 and 2 specifically
for testing student_app models
'''
from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from student_app.models import Student

#pylint: disable=no-member

#Part I
class TestStudent(TestCase):
    """ Class to test Student model field validation """
    def setUp(self):
        """ Method to create a test student profile """
        curr_student = Student.objects.create(
                name="Johnny H. Harris",
                student_email="thisIsMyEmail@school.com",
                personal_email="thisIsMyEmail@gmail.com",
                locker_number=108,
                locker_combination="11-11-11",
                good_student=False,
                )
        curr_student.save()

    def test_001_student_with_improper_good_student_field(self):
        """ Test to check good_student field validation """
        try:
            new_student = Student.objects.create(
                    name="John W. Watson",
                    student_email="thisIsAnEmail@school.com",
                    personal_email="thisIsAnEmail@gmail.com",
                    locker_number=13,
                    locker_combination="12-33-44",
                    good_student=None,
                    )

            new_student.full_clean()
            self.fail()
        except IntegrityError as e:
            print(e)
            self.assertIn(
                    #pylint: disable=line-too-long
                    'null value in column "good_student" of relation "student_app_student" violates not-null constraint',
                    str(e),
                    )

    def test_002_student_with_improper_email_fields(self):
        """ Test to check student_email and personal_email field validation """
        try:
            new_student = Student.objects.create(
                    name="John W. Watson",
                    student_email="thisIsNotAnEmail",
                    personal_email=False,
                    locker_number=13,
                    locker_combination="23-33-44",
                    good_student=True,
                    )
            new_student.full_clean()
            self.fail()
        except ValidationError as e:
            print(e.message_dict)
            self.assertTrue(
                    "student_email" in e.message_dict and "personal_email" in e.message_dict
                    )

    def test_003_student_with_improper_locker_number_fields(self):
       """ Test to check locker_number field validation """
       try:
           new_student = Student.objects.create(
                   name="John W. Watson",
                   student_email="thisIsAnEmail@school.com",
                   personal_email="thisIsAnEmail@gmail.com",
                   locker_number="None",
                   locker_combination="23-33-44",
                   good_student=True,
            )
           new_student.full_clean()
           self.fail()
            #pylint: disable=broad-except
       except Exception as e:
           self.assertTrue(
                   "Field 'locker_number' expected a number but got 'None'" in str(e)
            )

    def test_004_student_with_improper_locker_combination_fields(self):
        """ Test to check locker_combination field validation """
        try:
            new_student = Student.objects.create(
                    name="John W. Watson",
                    student_email="thisIsAnEmail@school.com",
                    personal_email="thisIsAnEmail@gmail.com",
                    locker_number=13,
                    locker_combination=None,
                    good_student=True,
                    )
            new_student.full_clean()
            self.fail()
        except IntegrityError as e:
            print(e)
            self.assertTrue('null value in column "locker_combination" ' in str(e))

    def test_005_student_with_improper_name_field(self):
        """ Test to check name field validation """
        try:
            new_student = Student.objects.create(
                    name = None,
                    student_email="thisIsAnEmail@school.com",
                    personal_email="thisIsAnEmail@gmail.com",
                    locker_number=13,
                    locker_combination="12-12-12",
                    good_student=True,
                    )
            new_student.full_clean()
            self.fail()
            # pylint: disable=broad-except
        except Exception as e:
            self.assertTrue('null value in column "name" ' in str(e))

    def test_006_student_with_proper_fields(self):
        """ Test to check all fields with proper values """
        new_student = Student.objects.create(
                name="John W. Wally",
                student_email="john@school.com",
                personal_email="john@gmail.com",
                locker_number=13,
                locker_combination="12-12-12",
                good_student=True,
                )
        new_student.full_clean()
        self.assertIsNotNone(new_student)

    # Part II
    def test_007_student_with_repeated_student_email(self):
        """ Test to check unique constraint on student_email field """
        try:
            new_student = Student.objects.create(
                    name="Johnny H. Harris",
                    student_email="thisIsMyEmail@school.com",
                    personal_email="myEmail@gmail.com",
                    locker_number=109,
                    locker_combination="11-11-11",
                    good_student=False,
                    )
            new_student.full_clean()
            self.fail()
        except IntegrityError as e:
            self.assertTrue("student_app_student_student_email" in str(e))

    def test_008_student_with_repeated_personal_email(self):
        """ Test to validate unique email address requirements """
        try:
            new_student = Student.objects.create(
                    name="Johnny H. Harris",
                    student_email="IsMyEmail@school.com",
                    personal_email="thisIsMyEmail@gmail.com",
                    locker_number=109,
                    locker_combination="11-11-11",
                    good_student=False,
                    )
            new_student.full_clean()
            self.fail()
        except IntegrityError as e:
            self.assertTrue("student_app_student_personal_email" in str(e))

    def test_009_student_with_repeated_locker_number(self):
        """ Test to check unique constraint on locker_number field """
        try:
            new_student = Student.objects.create(
                    name="Johnny H. Harris",
                    student_email="IsyEmail@school.com",
                    personal_email="tIsMyEmail@gmail.com",
                    locker_number=108,
                    locker_combination="11-11-11",
                    good_student=False,
                    )
            new_student.full_clean()
            self.fail()
        except IntegrityError as e:
            self.assertTrue("student_app_student_locker_number" in str(e))

    def test_010_student_utilizing_default_values(self):
        """ Test to check creation of student utilizing default field values """
        new_student = Student.objects.create(
                name="Maverick H. Macconnel",
                student_email="mav@school.com",
                personal_email="mav@gmail.com",
                )
        new_student.full_clean()
        self.assertIsNotNone(new_student)

