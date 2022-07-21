from django.urls import include, path
from .views import QuoteModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('quote', QuoteModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
