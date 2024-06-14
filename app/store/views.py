"""Store Views"""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Items,
)
from .serializer import (
    ItemsSerializer,
)


class ItemsViewsets(viewsets.ModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    permission_classes= [IsAuthenticated]
