from rest_framework.test import APITestCase
from rest_framework import status
from django.conf import settings
from datetime import date, timedelta
from collections import OrderedDict
from ..models.client import Client
from ..models.book import Book
from ..models.reserve import Reserve
from ..models.Interest import Interest


class ClientBookTestCase(APITestCase):
    URL = '/v1/client/{}/book'

    def setUp(self):
        self.model_client = Client.objects.create(name='Jhon Watson')
        self.model_book = Book.objects.create(title='Harry Potter')
        Interest.objects.create(days=1, fine=3.0, interest=0.2)
        Interest.objects.create(days=4, fine=5.0, interest=0.4)
        Interest.objects.create(days=7, fine=7.0, interest=0.6)

    def test_get_book_zero_day(self):
        self.model_reserve = Reserve.objects.create(
            client=self.model_client,
            book=self.model_book)
        self.response = self.client.get(self.URL.format(self.model_client.id))
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        results = self.response.data['results'][0]
        self.assertEqual(results['fine'], 0)
        self.assertEqual(results['interest'], 0)

    def test_get_book_one_day_late(self):
        self.model_reserve = Reserve.objects.create(
            client=self.model_client,
            book=self.model_book)
        self.model_reserve.reserve_date = date.today() - timedelta(days=int(settings.DAYS_LENT) + 1)
        self.model_reserve.save()
        self.response = self.client.get(self.URL.format(self.model_client.id))
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        results = self.response.data['results'][0]
        self.assertEqual(results['fine'], 0.3)
        self.assertEqual(results['interest'], 0.02)

    def test_get_book_four_day_late(self):
        self.model_reserve = Reserve.objects.create(
            client=self.model_client,
            book=self.model_book)
        self.model_reserve.reserve_date = date.today() - timedelta(days=int(settings.DAYS_LENT) + 4)
        self.model_reserve.save()
        self.response = self.client.get(self.URL.format(self.model_client.id))
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        results = self.response.data['results'][0]
        self.assertEqual(results['fine'], 0.5)
        self.assertEqual(results['interest'], 0.16)
