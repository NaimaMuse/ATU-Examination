from django import forms
from .models import *

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'code', 'credit_hours', 'faculty']

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['name', 'start_date', 'end_date']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'batch', 'course', 'contact_details']

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = ['name', 'faculty_id', 'department', 'course_taught']



