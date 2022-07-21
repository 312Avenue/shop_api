from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('catalog', CatalogViews)
router.register('advatages', AdvatagesViews)
router.register('econom', EconomViews)
router.register('furniture', FurnitureViews)

urlpatterns = []
urlpatterns += router.urls # urlpatterns.extend(router.urls)