from django.contrib import admin
from .models import Course, Section, Lesson

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    list_filter  = ('course',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'section', 'order')
    list_filter  = ('section',)
    fields = ('section', 'title', 'file_path', 'order')  # 👈 added file_path
