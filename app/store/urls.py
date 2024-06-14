"""Url class for the sotre API's"""

from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    ItemsViewsets
)

router = DefaultRouter()
router.register('items', ItemsViewsets)

app_name = 'store'

urlpatterns = [
    path('', include(router.urls)),
]