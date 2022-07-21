from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import Quote
from .serializers import QuoteSerializer


class QuoteModelViewSet(viewsets.GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    """ API Viewset that allows POST, GET & LIST through mixins """

    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
