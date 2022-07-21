from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, ListModelMixin

from .models import Quote
from .serializers import QuoteSerializer


class QuoteModelViewSet(viewsets.GenericViewSet, CreateModelMixin, RetrieveModelMixin, ListModelMixin):
    """ API Viewset that allows POST, GET & LIST through mixins """

    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
