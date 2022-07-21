from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

# Catalog
class CatalogViews(ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


# Advatages
class AdvatagesViews(ModelViewSet):
    queryset = Advantages.objects.all()
    serializer_class = AdvantagesSerializer


# Econom
class EconomViews(ModelViewSet):
    queryset = Econom.objects.all()
    serializer_class = EconomSerializer


# Furniture
class FurnitureViews(ModelViewSet):
    queryset = Furniture.objects.all()
    serializer_class = FurnitureSerializer