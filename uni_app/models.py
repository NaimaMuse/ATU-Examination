from django.db import models
class Faculty(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    faculty_id = models.CharField(max_length=20, unique=True)
    course_taught =models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Semester(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
class Course(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10, unique=True)
    credit_hours = models.PositiveIntegerField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    batch = models.CharField(max_length=10)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    contact_details = models.TextField()

    def __str__(self):
        return self.name
