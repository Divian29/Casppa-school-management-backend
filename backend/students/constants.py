from django.db import models


class StudentAction(models.TextChoices):
    CREATED = "CREATED", "Created"
    PROMOTED = "PROMOTED", "Promoted"
    GRADUATED = "GRADUATED", "Graduated"
    SUSPENDED = "SUSPENDED", "Suspended"
    WITHDRAWN = "WITHDRAWN", "Withdrawn"
    DEACTIVATED = "DEACTIVATED", "Deactivated"
    READMITTED = "READMITTED", "Readmitted"