from rest_framework import serializers

from .models import Student, StudentStatus


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        fields = [
            "id",
            "school",
            "admission_number",
            "first_name",
            "last_name",
            "date_of_birth",
            "gender",
            "photo",
            "student_class",
            "house",
            "parent",
            "status",
            "admission_date",
        ]

        read_only_fields = [
            "status",
            "admission_date",
        ]

class ChangeStudentStatusSerializer(serializers.Serializer):

    status = serializers.ChoiceField(
        choices=StudentStatus.choices
    )

    reason = serializers.CharField(
        required=False,
        allow_blank=True
    )

class CSVUploadSerializer(serializers.Serializer):
    file = serializers.FileField()