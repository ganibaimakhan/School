from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.TextChoices):
    STUDENT = "STUDENT"
    TEACHER = "TEACHER"
    VP = "VP"
    PRINCIPAL = "PRINCIPAL"

class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="classes")

    def __str__(self):
        return f"{self.name} - {self.school.name}"

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=Role.choices)
    name = models.CharField(max_length=20, null=True, blank=True)
    surname = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    class_belong = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

class Teacher(models.Model):
    username = models.CharField(max_length=100, unique=True)
    class_belong = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)
    subject_belong = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True, blank=True)
