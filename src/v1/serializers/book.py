from rest_framework import serializers
from django.db import transaction
from ..models.book import Book
from ..models.reserve import Reserve


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'status']


class BookReserveSerializer(serializers.ModelSerializer):

    def validate_status(self, book):
        if book.status == Book.STATUS_LENT:
            raise serializers.ValidationError({'erro:': 'Este livro já está emprestado'})

    def create(self, validated_data):
        with transaction.atomic():
            book = Book.objects.get(pk=self.context["view"].kwargs["book_pk"])
            validated_data["book"] = book
            self.validate_status(book)
            reserve = Reserve.objects.create(**validated_data)
            book.status = Book.STATUS_LENT
            book.save()
            return reserve

    class Meta:
        model = Reserve
        fields = ['id', 'client', 'reserve_date']
