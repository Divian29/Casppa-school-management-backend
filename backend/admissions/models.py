from django.db import models

from schools.models import School, SchoolClass


class AdmissionStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"


class AdmissionApplication(models.Model):

    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="admission_applications"
    )

    first_name = models.CharField(
        max_length=100
    )

    last_name = models.CharField(
        max_length=100
    )

    date_of_birth = models.DateField()

    gender = models.CharField(
        max_length=20
    )

    desired_class = models.ForeignKey(
        SchoolClass,
        on_delete=models.PROTECT,
        related_name="applications"
    )

    parent_name = models.CharField(
        max_length=200
    )

    parent_email = models.EmailField()

    parent_phone = models.CharField(
        max_length=20
    )

    address = models.TextField(
        blank=True
    )

    status = models.CharField(
        max_length=20,
        choices=AdmissionStatus.choices,
        default=AdmissionStatus.PENDING
    )

    rejection_reason = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )


    class Meta:
        ordering = [
            "-created_at"
        ]


    def __str__(self):
        return f"{self.first_name} {self.last_name}"