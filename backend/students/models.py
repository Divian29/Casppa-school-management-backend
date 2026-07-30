from django.db import models

from parents.models import Parent
from schools.models import School, SchoolClass, House
from .constants import StudentAction

class Gender(models.TextChoices):
    MALE = "MALE", "Male"
    FEMALE = "FEMALE", "Female"


class StudentStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Active"
    SUSPENDED = "SUSPENDED", "Suspended"
    WITHDRAWN = "WITHDRAWN", "Withdrawn"
    DEACTIVATED = "DEACTIVATED", "Deactivated"
    GRADUATED = "GRADUATED", "Graduated"
    ALUMNI = "ALUMNI", "Alumni"

class Student(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="students"
    )

    admission_number = models.CharField(
        max_length=50
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=10,
        choices=Gender.choices,
    )

    photo = models.ImageField(
        upload_to="students/",
        blank=True,
        null=True
    )

    student_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.PROTECT,
        related_name="students"
    )

    house = models.ForeignKey(
        House,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )

    parent = models.ForeignKey(
        Parent,
        on_delete=models.SET_NULL,
        null=True,
        related_name="children"
    )

    status = models.CharField(
        max_length=20,
        choices=StudentStatus.choices,
        default=StudentStatus.ACTIVE
    )

    admission_date = models.DateField(
        auto_now_add=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "school",
                    "admission_number"
                ],
                name="unique_student_admission_number_per_school"
            )
        ]

        ordering = [
            "first_name",
            "last_name"
        ]


    def __str__(self):
        return (
            f"{self.first_name} "
            f"{self.last_name} "
            f"({self.admission_number})"
        )
    
class StudentHistory(models.Model):

    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="history"
    )

    action = models.CharField(
    max_length=20,
    choices=StudentAction.choices
    )

    reason = models.TextField(
        blank=True
    )

    previous_status = models.CharField(
        max_length=20,
        choices=StudentStatus.choices,
        blank=True
    )

    new_status = models.CharField(
        max_length=20,
        choices=StudentStatus.choices,
        blank=True
    )

    performed_by = models.CharField(
        max_length=100,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = [
            "-created_at"
        ]


    def __str__(self):
        return f"{self.student} - {self.action}"