from rest_framework import serializers

from .models import Student, StudentStatus


class StudentSerializer(serializers.ModelSerializer):

    school_name = serializers.CharField(
        source="school.name",
        read_only=True
    )

    student_class_name = serializers.CharField(
        source="student_class.name",
        read_only=True
    )

    house_name = serializers.CharField(
        source="house.name",
        read_only=True
    )

    parent_name = serializers.SerializerMethodField()


    def get_parent_name(self, obj):
        if obj.parent:
            return f"{obj.parent.first_name} {obj.parent.last_name}"
        return None


    class Meta:
        model = Student

        fields = [
            "id",
            "school",
            "school_name",
            "admission_number",
            "first_name",
            "last_name",
            "date_of_birth",
            "gender",
            "photo",
            "student_class",
            "student_class_name",
            "house",
            "house_name",
            "parent",
            "parent_name",
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