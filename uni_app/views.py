from django.shortcuts import render,get_list_or_404,get_object_or_404,redirect
from django.http import HttpResponse
from.models import *
from.forms import *

def home(request):
    return render(request,'base.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# Create View
def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})

# Update View
def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})

# Delete View
def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'course_confirm_delete.html', {'course': course})



def search_courses(request):
    query = request.GET.get('q')
    courses = Course.objects.filter(title__icontains=query) if query else Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})

def semester_list(request):
    semesters = Semester.objects.all()
    return render(request, 'semester_list.html', {'semesters': semesters})

def add_semester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm()
    return render(request, 'semester_form.html', {'form': form})

def edit_semester(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm(instance=semester)
    return render(request, 'semester_form.html', {'form': form})

def delete_semester(request, pk):
    semester = get_object_or_404(Semester, pk=pk)
    if request.method == 'POST':
        semester.delete()
        return redirect('semester_list')
    return render(request, 'semester_confirm_delete.html', {'semester': semester})

def dashboard_overview(request):
    course_count = Course.objects.count()
    semester_count = Semester.objects.count()
    student_count = Student.objects.count()
    faculty_count = Faculty.objects.count()
    
    context = {
        'course_count': course_count,
        'semester_count': semester_count,
        'student_count': student_count,
        'faculty_count': faculty_count,
    }
    
    return render(request, 'dashboard.html', context)

def student_list(request):
    students = Student.objects.all()
    query = request.GET.get('q')
    if query:
        students = students.filter(name__icontains=query) | students.filter(student_id__icontains=query) | students.filter(batch__icontains=query) | students.filter(course__name__icontains=query)
    return render(request, 'student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})


def faculty_list(request):
    query = request.GET.get('q')
    faculties = Faculty.objects.all()

    if query:
        faculties = faculties.filter(name__icontains=query) | faculties.filter(department__icontains=query)

    return render(request, 'faculty_list.html', {'faculties': faculties})

def add_faculty(request):
    if request.method == "POST":
        form = FacultyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_list')
    else:
        form = FacultyForm()
    return render(request, 'add_faculty.html', {'form': form})



