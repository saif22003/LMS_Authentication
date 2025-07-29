from django.contrib import admin
from .models import TeacherModel

@admin.register(TeacherModel)


class TeacherAdmin(admin.ModelAdmin):
    
    ordering = ["id"]
    
    list_filter = (
        "teacher_phone",
        )
    
    search_fields = (
        "teacher_phone",
        "status",
    )