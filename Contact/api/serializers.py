from rest_framework import serializers
from ..models import Contact


class ContacttSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'
