from rest_framework import serializers
from .models import Student, Teacher, School, Subject, Class, User
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'id',
            'username',
            'class_belong',
        )
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            'id',
            'username',
            'class_belong',
            'subject_belong'
        )
class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = (
            'id',
            'name',
        )