from django.db import models
from _applib.model_choices_fields import GenderChoice, TeacherStatus, PhoneValidator,DOBValidator


class TeacherModel(models.Model):
    full_name = models.CharField(max_length=30)
    teacher_phone = models.CharField(max_length=11,validators=[PhoneValidator()],unique=True)
    profile_picture = models.CharField(max_length=300)
    gender = models.CharField(max_length=10, choices=GenderChoice.choices, default=GenderChoice.MALE)
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        validators=[DOBValidator()]
    )
    website = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=15, choices=TeacherStatus.choices, default=TeacherStatus.PENDING)
    password = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Full Name: {self.full_name} || Teacher phone: {self.teacher_phone} || Status: {self.status}"
    
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
        db_table = "teacher"