from rest_framework.generics import CreateAPIView
from rest_framework import generics
from . import serializers
from ..models import Invoice
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Invoice List Of api.


class IInvoice(generics.ListCreateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'plate_number': ['exact'],
        'invoice_type': ['exact'],
        'invoice_number': ['exact'],
        'vin': ['exact'],
        'date': ['exact'],

    }
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['plate_number', 'invoice_number', 'vin', 'invoice_type']


class Dinvoice(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = serializers.InvoiceSerializer
