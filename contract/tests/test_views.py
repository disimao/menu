import json
import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from contract.models import (
    Client,
    Request,
    )


class ClientTests(APITestCase):
    def test_create_client(self):
        """
        Ensure we can create a new Client object.
        """
        url = reverse('client-list')
        data = {
            'email': 'diogosimaos@hotmail.com',
            'first_name': 'Diogo',
            'last_name': 'Simão',
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().email, 'diogosimaos@hotmail.com')


    def test_create_request(self):
        """
        Ensure we can create a new Request object.
        """
        url = reverse('client-list')
        client_data = {
            'email': 'diogosimaos@hotmail.com',
            'first_name': 'Diogo',
            'last_name': 'Simão',
            }
        response = self.client.post(url, client_data, format='json')
        response = json.loads(response.content)
        request_data = {
            'request_date': datetime.datetime.date(datetime.datetime.today()),
            'status': 'open',
            'client': response.get('id'),
        }

        url = reverse('request-list')
        response = self.client.post(url, request_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Request.objects.count(), 1)
        self.assertEqual(Request.objects.get().client.id, Client.objects.get().id)
