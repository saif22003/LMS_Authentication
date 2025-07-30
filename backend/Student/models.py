from django.db import models
from _applib.model_choices_fields import GenderChoice, PhoneValidator, DOBValidator


class StudentModel(models.Model):
    full_name = models.CharField(max_length=30)
    student_phone = models.CharField(max_length=11,validators=[PhoneValidator()],unique=True)
    profile_picture = models.CharField(max_length=300)
    gender = models.CharField(max_length=10, choices=GenderChoice.choices, default=GenderChoice.MALE)
    date_of_birth = models.DateField( null=True, blank=True, validators=[DOBValidator()])
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Full Name: {self.full_name} || Student phone: {self.student_phone}"
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        db_table = "student"
