import datetime

from django.test import TestCase
from contract.models import (
    Client,
    Request,
    )


class ModelsTestCase(TestCase):
    def test_create_client(self):
        client = Client.objects.create(email='diogosimaos@hotmail.com')
        client.first_name = 'Diogo'
        client.last_name = 'Simão'
        client.save()
        self.assertEqual(client.email, 'diogosimaos@hotmail.com')

    def test_create_request(self):
        client = Client.objects.create(email='diogosimaos@hotmail.com')
        client.first_name = 'Diogo'
        client.last_name = 'Simão'
        client.save()

        request = Request.objects.create(request_date=datetime.datetime.date(datetime.datetime.today()), client=client)
        request.save()
        self.assertEqual(request.request_date, datetime.datetime.date(datetime.datetime.today()))
