from notifications.models import Notification

from .constants import StudentAction
from schools.models import SchoolClass
from .models import Student, StudentHistory,StudentStatus
from alumni.models import Alumni


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


     StudentHistory.objects.create(

        student=student,

        action=new_status,

        previous_status=previous_status,

        new_status=new_status,

        reason=reason,

        performed_by="Admin"

     )


     if student.parent:

        Notification.objects.create(

            parent=student.parent,

            title="Student Status Updated",

            message=(
                f"{student.first_name} {student.last_name} "
                f"status changed to {new_status}."
            ),

            notification_type="STUDENT"

        )


     return student
    
    @staticmethod
    def promote_students(school, current_class):

        students = Student.objects.filter(
            school=school,
            student_class=current_class,
            status="ACTIVE"
        )


        next_class = SchoolClass.objects.filter(
            school=school,
            order=current_class.order + 1
        ).first()


        if not next_class:
            return {
                "success": False,
                "message": "No next class found."
            }


        promoted_count = 0


        for student in students:

            previous_class = student.student_class.name


            student.student_class = next_class
            student.save()


            StudentHistory.objects.create(

                student=student,

                action="PROMOTED",

                previous_status=student.status,

                new_status=student.status,

                reason=f"Promoted from {previous_class} to {next_class.name}",

                performed_by="Admin"

            )


            promoted_count += 1


        return {
            "success": True,
            "promoted_count": promoted_count,
            "from_class": current_class.name,
            "to_class": next_class.name
        }
    
    @staticmethod
    def graduate_students(school, final_class):

        students = Student.objects.filter(
            school=school,
            student_class=final_class,
            status=StudentStatus.ACTIVE
        )


        if not students.exists():

            return {
                "success": False,
                "message": "No active students found in this class."
            }


        graduated_count = 0


        for student in students:

            previous_status = student.status


            student.status = StudentStatus.GRADUATED
            student.save()


            Alumni.objects.get_or_create(
            student=student,
            defaults={
                "graduation_year": student.updated_at.year,
                "graduation_class": final_class.name,
                "email": student.parent.email if student.parent else None,
                "phone": student.parent.phone if student.parent else None,
                    }
            )


            StudentHistory.objects.create(
                student=student,
                action="GRADUATED",
                previous_status=previous_status,
                new_status=StudentStatus.GRADUATED,
                reason=f"Graduated from {final_class.name}",
                performed_by="Admin"
            )


            graduated_count += 1


        return {
            "success": True,
            "graduated_count": graduated_count,
            "class": final_class.name
        }