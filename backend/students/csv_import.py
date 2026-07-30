import csv
from io import TextIOWrapper
from datetime import datetime

from parents.models import Parent
from schools.models import House, SchoolClass, School

from .models import Student, Gender


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


        # Check required fields
        for field in required_fields:

            if not row.get(field):
                errors.append(
                    f"{field} is required."
                )


        if errors:
            return errors



        # Validate school
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