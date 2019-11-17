from rest_framework import serializers
from django.db.models import Sum, Avg, Max, Min, Count, F, Q
from ..models import Invoice


class InvoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invoice
        fields = '__all__'
