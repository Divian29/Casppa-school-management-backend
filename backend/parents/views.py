from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Parent
from .serializers import ParentSerializer


class ParentViewSet(ReadOnlyModelViewSet):

    queryset = Parent.objects.all()

    serializer_class = ParentSerializer