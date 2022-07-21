from rest_framework import status
from rest_framework.test import APITestCase
from acme_insurance.models import Quote
from unittest.mock import patch

class QuoteTests(APITestCase):

    def test_create_quote(self):
        """ Ensures new quote via POST request """

        url = '/quote/'
        data = {'effective_date': '2023-05-10',
                'has_cancelled': True,
                'owns_property': False,
                'state': 'Michigan',
                'zip_code': '23456-1234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quote.objects.count(), 1)
        self.assertEqual(Quote.objects.get().id, )



