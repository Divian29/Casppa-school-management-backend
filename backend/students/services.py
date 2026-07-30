from notifications.models import Notification

from .constants import StudentAction
from .models import StudentHistory


class StudentService:

    @staticmethod
    def create_student(student):
        StudentHistory.objects.create(
            student=student,
            action=StudentAction.CREATED,
            new_status=student.status,
            performed_by="Admin",
        )

        if student.parent:
            Notification.objects.create(
                parent=student.parent,
                title="Student Enrollment Successful",
                message=f"{student.first_name} {student.last_name} has been enrolled.",
                notification_type="STUDENT",
            )

        return student

    @staticmethod
    def change_status(student, new_status, reason=""):
        previous_status = student.status

        student.status = new_status
        student.save()

        status_action_map = {
            "ACTIVE": StudentAction.READMITTED,
            "SUSPENDED": StudentAction.SUSPENDED,
            "WITHDRAWN": StudentAction.WITHDRAWN,
            "DEACTIVATED": StudentAction.DEACTIVATED,
            "GRADUATED": StudentAction.GRADUATED,
            "ALUMNI": StudentAction.GRADUATED,
        }

        StudentHistory.objects.create(
            student=student,
            action=status_action_map.get(
                new_status,
                StudentAction.READMITTED,
            ),
            previous_status=previous_status,
            new_status=new_status,
            reason=reason,
            performed_by="Admin",
        )

        return student