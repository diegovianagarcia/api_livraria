from rest_framework import viewsets
from .models import Client, Book, Reserve, Interest
from .serializers import (
    ClientSerializer,
    BookSerializer,
    BookReserveSerializer,
    ClientReserveSerializer,
    InterestSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete', ]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # @action(methods=['post'], detail=True, serializer_class=BookReserveSerializer)
    # def reserve(self, request, pk=None):
    #     book = self.get_object()
    #     data = JSONParser().parse(request)
    #     serializer = BookReserveSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=200)
    #     return JsonResponse(serializer.errors, status=400)


class BookReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = BookReserveSerializer

    def get_queryset(self):
        return Reserve.objects.filter(book=self.kwargs['book_pk'])


class ClientReserveViewSet(viewsets.ModelViewSet):
    queryset = Reserve.objects.all()
    serializer_class = ClientReserveSerializer

    def get_queryset(self):
        return Reserve.objects.filter(client=self.kwargs['client_pk'])


class InterestViewSet(viewsets.ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer
