from rest_framework import viewsets
from ..models.book import Book
from ..models.reserve import Reserve
from ..serializers.book import BookSerializer, BookReserveSerializer


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
