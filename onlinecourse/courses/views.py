from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course, Lesson

def course_list(request):
    """
    Public homepage: shows all courses.
    """
    courses = Course.objects.all()
    # Debug prints (remove in production)
    print("✅ course_list view running, found courses:", courses)

    return render(request, 'courses/menu.html', {
        'courses': courses,
    })


def course_detail(request, course_pk):
    """
    Redirects to the first lesson of the course.
    """
    # Simply delegate to lesson_detail with no lesson_pk
    return lesson_detail(request, course_pk, lesson_pk=None)


def lesson_detail(request, course_pk, lesson_pk=None):
    """
    Udemy‑style course page:
    - Left sidebar: all sections & lessons
    - Main area: embedded video for the selected (or first) lesson
    """
    # 1) Load the course or 404
    course = get_object_or_404(Course, pk=course_pk)

    # 2) Eager‑load sections + their lessons
    sections = course.sections.prefetch_related('lessons').all()

    # 3) Pick which lesson to display
    if lesson_pk:
        lesson = get_object_or_404(
            Lesson,
            pk=lesson_pk,
            section__course=course
        )
    else:
        # Default: first lesson of first section (if any)
        first_section = sections.first()
        lesson = (
            first_section.lessons.first()
            if first_section and first_section.lessons.exists()
            else None
        )

    # Debug output
    print(f"➡️ lesson_detail: course={course_pk}, sections={len(sections)}, lesson={lesson}")

    # 4) Render the template with all context it needs
    return render(request, 'courses/course_detail.html', {
        'course':   course,
        'sections': sections,
        'lesson':   lesson,
    })
