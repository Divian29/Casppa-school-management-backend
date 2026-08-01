from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import School, SchoolClass, House
from .serializers import (
    SchoolSerializer,
    SchoolClassSerializer,
    HouseSerializer,
)


class SchoolViewSet(ReadOnlyModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolClassViewSet(ReadOnlyModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer


class HouseViewSet(ReadOnlyModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer