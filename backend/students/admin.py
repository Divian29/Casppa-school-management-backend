from django.contrib import admin

from .models import Student
from .models import Student, StudentHistory


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        "first_name",
        "last_name",
        "admission_number",
        "student_class",
        "status",
    )

    list_filter = (
        "status",
        "student_class",
        "school",
    )

    search_fields = (
        "first_name",
        "last_name",
        "admission_number",
    )

@admin.register(StudentHistory)
class StudentHistoryAdmin(admin.ModelAdmin):

    list_display = (
        "student",
        "action",
        "previous_status",
        "new_status",
        "created_at",
    )

    list_filter = (
        "action",
        "new_status",
    )