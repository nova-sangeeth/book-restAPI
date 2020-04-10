from . import models
from . import serializers
from rest_framework import viewsets

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


@permission_classes([IsAuthenticated])
class book_store_viewset(viewsets.ModelViewSet):
    queryset = models.book_store.objects.all()
    serializer_class = serializers.book_store_serializers
