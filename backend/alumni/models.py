from django.db import models

from students.models import Student


class Alumni(models.Model):

    student = models.OneToOneField(
        Student,
        on_delete=models.CASCADE,
        related_name="alumni_profile"
    )

    graduation_year = models.PositiveIntegerField()

    graduation_class = models.CharField(
        max_length=100
    )

    email = models.EmailField(
        blank=True,
        null=True
    )

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:

        ordering = [
            "-graduation_year"
        ]


    def __str__(self):

        return (
            f"{self.student.first_name} "
            f"{self.student.last_name}"
        )