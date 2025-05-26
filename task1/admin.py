from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import User, School, Subject, Class, Student, Teacher

admin.site.register(User)
admin.site.register(School)
admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)