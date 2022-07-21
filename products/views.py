from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import *
from .models import *

# Catalog
class CatalogViews(ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


# Hits
class HitsViews(ModelViewSet):
    queryset = Catalog.objects.all()
    serializer_class = HitsSerializer


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


# Pluses
class PlusesViews(ModelViewSet):
    queryset = Pluses.objects.all()
    serializer_class = PlusesSerializer


# Profit
class ProfitViews(ModelViewSet):
    queryset = Profit.objects.all()
    serializer_class = ProfitSerializer