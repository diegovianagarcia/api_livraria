from django.db import transaction
from rest_framework import serializers
from ..models.client import Client
from ..models.reserve import Reserve


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name']


class ClientReserveSerializer(serializers.ModelSerializer):
    book = serializers.CharField(source='book.title')

    class Meta:
        model = Reserve
        fields = ['book', 'reserve_date', 'fine', 'interest']
