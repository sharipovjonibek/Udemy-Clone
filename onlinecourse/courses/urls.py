# courses/urls.py
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    # 1) List all courses
    path(
        '',
        views.course_list,
        name='course_list'
    ),

    # 2) Show the first lesson of a course (no lesson_pk)
    #    e.g. GET /course/1/
    path(
        'course/<int:course_pk>/',
        views.lesson_detail,
        name='lesson_detail'
    ),

    # 3) Show a specific lesson by its pk
    #    e.g. GET /course/1/lesson/3/
    path(
        'course/<int:course_pk>/lesson/<int:lesson_pk>/',
        views.lesson_detail,
        name='lesson_detail'
    ),
]
