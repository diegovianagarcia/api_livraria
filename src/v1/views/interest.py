from rest_framework import viewsets
from ..models.Interest import Interest
from ..serializers.interest import InterestSerializer


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
