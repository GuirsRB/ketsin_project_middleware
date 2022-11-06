from rest_framework import serializers
from .models import *


class DeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'


class DocumentsDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentsDelivery
        fields = '__all__'


class DocumentKindSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentKind
        fields = '__all__'
