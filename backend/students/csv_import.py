import csv
from io import TextIOWrapper
from datetime import datetime

from django.db import transaction

from parents.models import Parent
from schools.models import House, SchoolClass, School

from notifications.models import Notification

from .models import Student, Gender, StudentHistory


class StudentCSVImporter:

    REQUIRED_COLUMNS = [
        "school",
        "admission_number",
        "first_name",
        "last_name",
        "date_of_birth",
        "gender",
        "class",
        "house",
        "parent_email",
    ]


    @classmethod
    def preview(cls, csv_file):

        reader = csv.DictReader(
            TextIOWrapper(
                csv_file.file,
                encoding="utf-8"
            )
        )


        missing = [
            column
            for column in cls.REQUIRED_COLUMNS
            if column not in reader.fieldnames
        ]


        if missing:
            return {
                "success": False,
                "errors": [
                    f"Missing required columns: {', '.join(missing)}"
                ]
            }


        preview = []

        valid_rows = 0
        invalid_rows = 0


        for index, row in enumerate(reader, start=1):

            errors = cls.validate_row(row)


            if errors:
                status = "INVALID"
                invalid_rows += 1

            else:
                status = "VALID"
                valid_rows += 1


            preview.append(
                {
                    "row": index,
                    "status": status,
                    "errors": errors,
                    "data": row,
                }
            )


        return {
            "success": True,
            "total_rows": len(preview),
            "valid_rows": valid_rows,
            "invalid_rows": invalid_rows,
            "preview": preview,
        }



    @classmethod
    def confirm(cls, csv_file):

        reader = csv.DictReader(
            TextIOWrapper(
                csv_file.file,
                encoding="utf-8"
            )
        )


        imported = []
        failed = []


        for index, row in enumerate(reader, start=1):

            errors = cls.validate_row(row)


            if errors:

                failed.append(
                    {
                        "row": index,
                        "errors": errors
                    }
                )

                continue


            try:

                with transaction.atomic():

                    school = School.objects.get(
                        id=row["school"]
                    )


                    student_class = SchoolClass.objects.get(
                        name=row["class"]
                    )


                    house = House.objects.get(
                        name=row["house"]
                    )


                    parent = Parent.objects.get(
                        email=row["parent_email"]
                    )


                    student = Student.objects.create(

                        school=school,

                        admission_number=row["admission_number"],

                        first_name=row["first_name"],

                        last_name=row["last_name"],

                        date_of_birth=row["date_of_birth"],

                        gender=row["gender"],

                        student_class=student_class,

                        house=house,

                        parent=parent,

                    )


                    StudentHistory.objects.create(

                        student=student,

                        action="STUDENT_CREATED",

                        new_status=student.status,

                        performed_by="Admin"

                    )


                    Notification.objects.create(

                        parent=parent,

                        title="Student Enrollment Successful",

                        message=f"{student.first_name} {student.last_name} has been enrolled.",

                        notification_type="STUDENT"

                    )


                    imported.append(
                        {
                            "row": index,
                            "student_id": student.id
                        }
                    )


            except Exception as e:


                failed.append(
                    {
                        "row": index,
                        "errors": [
                            str(e)
                        ]
                    }
                )


        return {

            "success": True,

            "imported_count": len(imported),

            "failed_count": len(failed),

            "imported": imported,

            "failed": failed

        }




    @classmethod
    def validate_row(cls, row):

        errors = []


        required_fields = [

            "school",

            "admission_number",

            "first_name",

            "last_name",

            "date_of_birth",

            "gender",

            "class",

            "house",

            "parent_email",

        ]


        for field in required_fields:

            if not row.get(field):

                errors.append(
                    f"{field} is required."
                )


        if errors:

            return errors



        # School validation

        if not School.objects.filter(
            id=row["school"]
        ).exists():

            errors.append(
                f"School '{row['school']}' does not exist."
            )



        # Duplicate admission number per school

        if Student.objects.filter(

            school_id=row["school"],

            admission_number=row["admission_number"]

        ).exists():

            errors.append(
                "Admission number already exists for this school."
            )



        # Gender validation

        valid_genders = [
            choice[0]
            for choice in Gender.choices
        ]


        if row["gender"] not in valid_genders:

            errors.append(
                "Invalid gender."
            )



        # Date validation

        try:

            datetime.strptime(
                row["date_of_birth"],
                "%Y-%m-%d"
            )

        except ValueError:

            errors.append(
                "Invalid date format. Use YYYY-MM-DD."
            )



        # Class validation

        if not SchoolClass.objects.filter(
            name=row["class"]
        ).exists():

            errors.append(
                f"Class '{row['class']}' does not exist."
            )



        # House validation

        if not House.objects.filter(
            name=row["house"]
        ).exists():

            errors.append(
                f"House '{row['house']}' does not exist."
            )



        # Parent validation

        if not Parent.objects.filter(
            email=row["parent_email"]
        ).exists():

            errors.append(
                f"Parent '{row['parent_email']}' does not exist."
            )


        return errors