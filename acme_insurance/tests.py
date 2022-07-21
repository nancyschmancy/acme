from rest_framework import status
from rest_framework.test import APITestCase
from acme_insurance.models import Quote
from acme.rates import rates

class QuoteTests(APITestCase):
    url = '/api/quote/'

    def test_create_quote(self):
        """ Ensures new quote via POST request """

        data = {'effective_date': '2023-05-10',
                'has_cancelled': True,
                'owns_property': False,
                'state': 'Michigan',
                'zip_code': '23456-1234'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quote.objects.count(), 1)

    def test_get_quote(self):
        """ Ensures quote retrieved via GET request """

        data = {'effective_date': '2025-12-22',
                'has_cancelled': False,
                'owns_property': False,
                'state': 'Oregon',
                'zip_code': '58634'}
        post_response = self.client.post(self.url, data, format='json')
        get_response = self.client.get('{}{}/'.format(self.url, post_response.data['id']))
        self.assertEqual(get_response.status_code, status.HTTP_200_OK)

    def test_invalid_state_field(self):
        """ Ensures error response when state cannot be validated """

        data = {'effective_date': '2023-05-10',
                'has_cancelled': True,
                'owns_property': False,
                'state': 'Yabbadabadoo',
                'zip_code': '23456-1234'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_zip_code_field(self):
        """ Ensures zip code is correct format """

        data = {'effective_date': '2023-05-10',
                'has_cancelled': True,
                'owns_property': False,
                'state': 'TX',
                'zip_code': 'ABCDEFG'}

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_rate_calculation(self):
        """ Ensures rate calculation """

        data = {'effective_date': '2023-05-10',
                'has_cancelled': False,  # 10% discount
                'owns_property': False,  # 0 discount
                'state': 'TX',  # 0 fees added
                'zip_code': '12345'
                }
        post_response = self.client.post(self.url, data, format='json')
        get_response = self.client.get('{}{}/'.format(self.url, post_response.data['id']))
        self.assertEqual(float(get_response.data['total_term_premium']), round(rates.BASE_TERM_RATE * .9, 2))
