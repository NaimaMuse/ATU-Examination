from django.urls import path
from.views import *

urlpatterns =[
    path('',dashboard_overview, name='dashboard_overview'),
    path('courses/', course_list, name='course_list'),
    path('courses/add/', course_add, name='course_add'),
    path('courses/<int:pk>/update/', course_update, name='course_update'),
    path('courses/<int:pk>/delete/', course_delete, name='course_delete'),
    path('semesters/', semester_list, name='semester_list'),
    path('semesters/add/', add_semester, name='add_semester'),
    path('semesters/edit/<int:pk>/', edit_semester, name='edit_semester'),
    path('semesters/delete/<int:pk>/', delete_semester, name='delete_semester'),
    path('students/', student_list, name='student_list'),
    path('students/add/', student_add, name='student_add'),
    path('students/edit/<int:pk>/', student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', student_delete, name='student_delete'),
    path('faculties/', faculty_list, name='faculty_list'),
    path('faculties/add/', add_faculty, name='add_faculty'),

  

]