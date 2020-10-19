from rest_framework.test import APITestCase
from rest_framework import status
from collections import OrderedDict
from .test_book import BookBuilder
from ..models.client import Client
from ..models.book import Book


class ReserveBuilder():

    @staticmethod
    def new_reserve_body(client='1') -> dict:
        return {
            'client': client
        }


class ReserveTestCase(APITestCase):
    URL = '/v1/book/{}/reserve'

    def setUp(self):
        self.model_client = Client.objects.create(name='Jhon Watson')
        self.model_book = Book.objects.create(title='Harry Potter')

    def test_post_reserve(self):
        '''
        Reservar um livro com sucesso
        '''
        self.body = ReserveBuilder.new_reserve_body(client=self.model_client.id)
        self.response = self.client.post(self.URL.format(self.model_book.id), self.body)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_post_reserve_error(self):
        '''
        Reservar um livro com erro: O livro já está emprestado
        '''
        self.test_post_reserve()
        self.response = self.client.post(self.URL.format(self.model_book.id), self.body)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(self.response.data, {'erro:': 'Este livro já está emprestado'})
