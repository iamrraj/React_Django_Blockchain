from rest_framework.generics import CreateAPIView
from rest_framework import generics
from . import serializers
from ..models import Campaign
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Invoice List Of api.


class CCamp(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = serializers.CampaignSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'campname': ['exact'],
        'camptype': ['exact'],
        'parameters': ['exact'],
        'candidate': ['exact'],
        'prize': ['exact'],

    }
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['plate_number', 'invoice_number', 'vin', 'invoice_type']


class DDCamp(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = serializers.CampaignSerializer
