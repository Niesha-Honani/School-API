from django.db import models

# Create your models here.

class Student(models.Model):
    # Fields for student_app
    name = models.CharField(max_length=255)
    student_email = models.CharField(max_length=255)
    personal_email = models.CharField(max_length=255)
    locker_number = models.IntegerField(unique=True)
    locker_combination = models.CharField(default="12-12-12")

    good_student=models.BooleanField(unique = False, default=True)
    
    # foreign key class model
    #classes = models.ManyToManyField('class_app.Class', related_name='students')


    # __str__ method : Returns student name, student email and locker number as
    # "John W. Watson - johnnyBoy@school.com - 137"

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"

    # locker assignment method: Takes in an int representing locker number and
    # adds locker number to student
    def locker_reassignment(self, new_locker_number):
        self.locker_number = new_locker_number
        self.save()

    # student_status method: Takes in a bool representing if a student is
    # a good student and changes a students "good_student" property to said value
    def student_status(self, new_value):
        self.good_student = new_value


