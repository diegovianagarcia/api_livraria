from rest_framework.test import APITestCase
from rest_framework import status
from collections import OrderedDict
from ..models.book import Book


class BookBuilder():

    @staticmethod
    def new_book_body(title='Book') -> dict:
        return {
            'title': title
        }


class BookTestCase(APITestCase):
    URL = '/v1/book'

    def test_post_book(self):
        self.body = BookBuilder.new_book_body(title='Harry Potter')
        self.response = self.client.post(self.URL, self.body)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(self.response.data, {
            'id': 1,
            'title': self.body['title'],
            'status': Book.STATUS_AVAILABLE
        })

    def test_get_detail(self):
        self.test_post_book()
        data = self.response.data
        self.response = self.client.get(f'{self.URL}/{str(data["id"])}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(self.response.data, data)

    def test_get_list(self):
        self.test_post_book()
        book1 = self.body['title']
        self.body = BookBuilder.new_book_body(title='Percy Jackson')
        book2 = self.body['title']
        self.response = self.client.post(self.URL, self.body)
        self.response = self.client.get(self.URL)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertListEqual(self.response.data['results'], [OrderedDict(
            {
                'id': 1,
                'title': book1,
                'status': Book.STATUS_AVAILABLE
            }),
            OrderedDict({
                'id': 2,
                'title': book2,
                'status': Book.STATUS_AVAILABLE
            })
        ])
