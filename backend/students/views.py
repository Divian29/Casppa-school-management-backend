from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .csv_import import StudentCSVImporter
from .serializers import CSVUploadSerializer
from .models import StudentStatus
from schools.models import School
from schools.models import SchoolClass
from .models import StudentStatus

from .models import Student
from .serializers import (
    StudentSerializer,
    ChangeStudentStatusSerializer,
)
from .services import StudentService


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        student = serializer.save()

        StudentService.create_student(student)

        return Response(
            {
                "message": "Student created successfully",
                "student": StudentSerializer(student).data,
            },
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=True,
        methods=["post"],
        url_path="change-status",
    )
    def change_status(self, request, pk=None):
        student = self.get_object()

        serializer = ChangeStudentStatusSerializer(
            data=request.data
        )

        serializer.is_valid(raise_exception=True)

        StudentService.change_status(
            student=student,
            new_status=serializer.validated_data["status"],
            reason=serializer.validated_data.get("reason", ""),
        )

        return Response(
            {
                "message": "Student status updated successfully.",
                "student": StudentSerializer(student).data,
            }
        )
    
    @action(
        detail=False,
        methods=["post"],
        url_path="import/preview",
    )
    def preview_import(self, request):
        serializer = CSVUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = StudentCSVImporter.preview(
            serializer.validated_data["file"]
        )

        return Response(result)
    

    @action(
        detail=False,
        methods=["post"],
        url_path="import/confirm"
    )
    def import_confirm(self, request):

        csv_file = request.FILES.get("file")


        if not csv_file:

            return Response(
                {
                    "error": "CSV file is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


        result = StudentCSVImporter.confirm(
            csv_file
        )


        return Response(result)
    
    @action(
    detail=False,
    methods=["get"],
    url_path="active"
    )
    def active_students(self, request):

     students = Student.objects.filter(
        status=StudentStatus.ACTIVE
     )

     serializer = self.get_serializer(
        students,
        many=True
     )

     return Response(serializer.data)
    
    @action(
        detail=False,
        methods=["post"],
        url_path="promote"
    )
    def promote(self, request):

        school_id = request.data.get("school")
        class_id = request.data.get("class")


        school = School.objects.get(
            id=school_id
        )


        current_class = SchoolClass.objects.get(
            id=class_id
        )


        result = StudentService.promote_students(
            school,
            current_class
        )


        return Response(result)
    
    @action(
        detail=False,
        methods=["post"],
        url_path="graduate"
    )
    def graduate(self, request):

        school_id = request.data.get("school")
        class_id = request.data.get("class")


        if not school_id or not class_id:

            return Response(
                {
                    "error": "school and class are required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


        try:

            school = School.objects.get(
                id=school_id
            )


            final_class = SchoolClass.objects.get(
                id=class_id,
                school=school
            )


        except (
            School.DoesNotExist,
            SchoolClass.DoesNotExist
        ):

            return Response(
                {
                    "error": "School or class not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )


        result = StudentService.graduate_students(
            school=school,
            final_class=final_class
        )


        return Response(result)
    
    @action(
        detail=False,
        methods=["post"],
        url_path="promote"
    )
    def promote(self, request):

        school_id = request.data.get("school")
        class_id = request.data.get("class")


        if not school_id or not class_id:
            return Response(
                {
                    "error": "school and class are required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )


        try:

            school = School.objects.get(
                id=school_id
            )


            current_class = SchoolClass.objects.get(
                id=class_id,
                school=school
            )


        except (School.DoesNotExist, SchoolClass.DoesNotExist):

            return Response(
                {
                    "error": "School or class not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )


        result = StudentService.promote_students(
            school=school,
            current_class=current_class
        )


        return Response(result)
    
    @action(
        detail=False,
        methods=["post"],
        url_path="graduate"
    )
    def graduate(self, request):

        school_id = request.data.get("school")
        class_id = request.data.get("class")


        school = School.objects.get(
            id=school_id
        )

        final_class = SchoolClass.objects.get(
            id=class_id,
            school=school
        )


        result = StudentService.graduate_students(
            school=school,
            final_class=final_class
        )


        return Response(result)