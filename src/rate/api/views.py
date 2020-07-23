from rest_framework import generics

from rate.models import Rate
from rate.api.serializers import RateSerializer


class RateListCreateView(generics.ListCreateAPIView):
    # permission_classes = []
    # authentication_classes = []
    queryset = Rate.objects.all()
    serializer_class = RateSerializer


class RateReadUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
