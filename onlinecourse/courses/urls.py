# courses/urls.py
from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path(
        '',
        views.course_list,
        name='course_list'
    ),

    path(
        'course/<int:course_pk>/',
        views.lesson_detail,
        name='lesson_detail'
    ),

    path(
        'course/<int:course_pk>/lesson/<int:lesson_pk>/',
        views.lesson_detail,
        name='lesson_detail'
    ),
]
