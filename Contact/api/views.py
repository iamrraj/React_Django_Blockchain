from rest_framework.generics import CreateAPIView
from rest_framework import generics
from . import serializers
from ..models import Contact
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

# Invoice List Of api.


class CCustomer(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContacttSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'first_name': ['exact'],
        'last_name': ['exact']
    }


class DCustomer(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = serializers.ContacttSerializer
