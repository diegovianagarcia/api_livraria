from rest_framework import viewsets
from ..models.client import Client
from ..models.reserve import Reserve
from ..serializers.client import ClientSerializer, ClientReserveSerializer


class ClientViewSet(viewsets.ModelViewSet):
    # http_method_names = ['get', 'post', 'delete', ]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ClientReserveSerializer

    def get_queryset(self):
        return Reserve.objects.filter(client=self.kwargs['client_pk'])
