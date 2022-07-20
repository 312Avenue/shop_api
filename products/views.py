from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .serializers import CatalogSerializer
from .models import Catalog


class CatalogViews(mixins.ListModelMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer