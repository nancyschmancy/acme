from rest_framework import status
from rest_framework.test import APITestCase
from acme_insurance.models import Quote
from unittest.mock import patch


class QuoteTests(APITestCase):

    def test_create_quote(self):
        """ Ensures new quote via POST request """

        url = '/api/quote/'
        data = {'effective_date': '2023-05-10',
                'has_cancelled': True,
                'owns_property': False,
                'state': 'Michigan',
                'zip_code': '23456-1234'}
        response = self.client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quote.objects.count(), 1)

    def test_invalid_state_field(self):
        """ Ensures error response when state cannot be validated """

        url = '/api/quote/'
        data = {'effective_date': '2023-05-10',
                'has_cancelled': True,
                'owns_property': False,
                'state': 'Yabbadabadoo',
                'zip_code': '23456-1234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_zip_code_field(self):
        """ Ensures zip code is correct format """

        url = '/api/quote/'
        data = {'effective_date': '2023-05-10',
                'has_cancelled': True,
                'owns_property': False,
                'state': 'w v',
                'zip_code': 'ABCDEFG'}

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
