from django.db import models

from parents.models import Parent


class NotificationType(models.TextChoices):
    STUDENT = "STUDENT", "Student"
    ADMISSION = "ADMISSION", "Admission"
    PAYMENT = "PAYMENT", "Payment"
    GENERAL = "GENERAL", "General"


class Notification(models.Model):

    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name="notifications"
    )

    title = models.CharField(
        max_length=200
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=20,
        choices=NotificationType.choices,
        default=NotificationType.GENERAL
    )

    is_read = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    class Meta:
        ordering = [
            "-created_at"
        ]


    def __str__(self):
        return self.title