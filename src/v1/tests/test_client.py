from rest_framework.test import APITestCase
from rest_framework import status
from collections import OrderedDict
from ..models.client import Client


class ClientBuilder():

    @staticmethod
    def new_client_body(name='Client') -> dict:
        return {
            'name': name
        }


class ClientTestCase(APITestCase):
    URL = '/v1/client'

    def test_post_client(self):
        self.body = ClientBuilder.new_client_body(name='Harry Potter')
        self.response = self.client.post(self.URL, self.body)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertDictEqual(self.response.data, {
            'id': 1,
            'name': self.body['name'],
        })

    def test_get_by_detail(self):
        self.test_post_client()
        data = self.response.data
        self.response = self.client.get(f'{self.URL}/{str(data["id"])}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(self.response.data, data)

    def test_get_by_list(self):
        self.test_post_client()
        client1 = self.body['name']
        self.body = ClientBuilder.new_client_body(name='Percy Jackson')
        client2 = self.body['name']
        self.response = self.client.post(self.URL, self.body)
        self.response = self.client.get(self.URL)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertListEqual(self.response.data['results'], [OrderedDict(
            {
                'id': 1,
                'name': client1,
            }),
            OrderedDict({
                'id': 2,
                'name': client2,
            })
        ])
