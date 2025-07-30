from django.contrib import admin
from .models import StudentModel

@admin.register(StudentModel)


class StudentModel(admin.ModelAdmin):
    
    ordering = ["id"]
    
    list_filter = (
        "student_phone",
        )
    
    search_fields = (
        "student_phone",
    )
