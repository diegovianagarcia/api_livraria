from rest_framework import serializers
from ..models.Interest import Interest


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = ['id', 'days', 'fine', 'interest']
