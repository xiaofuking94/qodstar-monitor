from .serializers import DateDataSerializer
from .models import DateData

from rest_framework import viewsets


class DateDateViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DateDataSerializer
    queryset = DateData.objects.all()
