from django.urls import include, path
from .views import QuoteModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('quote', QuoteModelViewSet, basename='quote')

urlpatterns = [
    path('acme/', include(router.urls)),
]
