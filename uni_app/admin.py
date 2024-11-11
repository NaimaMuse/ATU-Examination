from django.contrib import admin
from .models import *
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'credit_hours')

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')

@admin.register(Semester)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date','end_date')

@admin.register(Student)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'student_id','batch','course','contact_details')


