from django.shortcuts import render, get_object_or_404
from django.conf import settings
from supabase import create_client
from .models import Course, Lesson


sb = create_client(settings.SUPABASE_URL, settings.SUPABASE_SERVICE_KEY)

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/menu.html', {
        'courses': courses,
    })


def lesson_detail(request, course_pk, lesson_pk=None):
    course = get_object_or_404(Course, pk=course_pk)
    sections = course.sections.prefetch_related('lessons').all()

    if lesson_pk:
        lesson = get_object_or_404(Lesson, pk=lesson_pk, section__course=course)
    else:
        first_section = sections.first()
        lesson = first_section.lessons.first() if first_section and first_section.lessons.exists() else None


    open_section_id = lesson.section.id if lesson else (sections.first().id if sections else None)

    signed_url = None
    if lesson and lesson.file_path:
        try:
            signed_url = sb.storage.from_(settings.SUPABASE_BUCKET).create_signed_url(
                lesson.file_path,
                3600  
            )["signedURL"]
        except Exception as e:
            print("⚠️ Supabase signed URL error:", e)

    return render(request, 'courses/course_detail.html', {
        'course': course,
        'sections': sections,
        'lesson': lesson,
        'signed_url': signed_url,
        'open_section_id': open_section_id,
    })
