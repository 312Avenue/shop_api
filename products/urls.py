from django.urls import path
from .views import CatalogViews

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('products', CatalogViews)

urlpatterns = []
urlpatterns += router.urls # urlpatterns.extend(router.urls)