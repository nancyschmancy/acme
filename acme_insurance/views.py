from rest_framework import viewsets

from .models import Quote
from .serializers import QuoteSerializer


class QuoteModelViewSet(viewsets.ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()
