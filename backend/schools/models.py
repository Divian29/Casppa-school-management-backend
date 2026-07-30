from django.db import models
from .constants import CLASS_LEVELS


class School(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name
    
class SchoolClass(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="classes",
    )

    name = models.CharField(max_length=100)

    level = models.CharField(
        max_length=20,
        choices=CLASS_LEVELS,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("school", "name")
        ordering = ["level", "name"]

    def __str__(self):
        return self.name
    
class House(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="houses",
    )

    name = models.CharField(max_length=100)

    color = models.CharField(max_length=30, blank=True)

    class Meta:
        unique_together = ("school", "name")

    def __str__(self):
        return self.name