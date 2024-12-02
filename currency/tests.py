from django.test import TestCase
from django.urls import reverse
from .models import Currency, Currencypair, ExchangeRate
from datetime import datetime

#testy stworzone przez chatgpt openai
class ApiTests(TestCase):
    
    def setUp(self):
        # Create Currency objects for USD, EUR, and PLN
        usd = Currency.objects.create(code="USD")
        eur = Currency.objects.create(code="EUR")
        pln = Currency.objects.create(code="PLN")
        
        # Create Currencypair (USD-EUR)
        usd_eur = Currencypair.objects.create(pair_code="USDEUR", base_currency=usd, quote_currency=eur)
        ExchangeRate.objects.create(currency_pair=usd_eur, exchange_rate=0.85, timestamp=datetime.now())
    
    def test_get_currencies(self):
        """
        Test that the API returns a list of currencies.
        """
        response = self.client.get(reverse('get_currencies'))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn({"code": "USD"}, response_data)
        self.assertIn({"code": "EUR"}, response_data)
        self.assertIn({"code": "PLN"}, response_data)

    def test_get_currency_pairs(self):
        """
        Test that the API returns a list of related currency pairs for a given currency.
        """
        response = self.client.get(reverse('get_currency_pairs', kwargs={'currency': 'USD'}))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("EUR", response_data["related_currencies"])

    def test_get_exchange_rate(self):
        """
        Test that the API returns the exchange rate for a specific currency pair.
        """
        response = self.client.get(reverse('get_exchange_rate', kwargs={'base': 'USD', 'quote': 'EUR'}))
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        
        # Check that the exchange rate is returned for the USD-EUR pair
        self.assertIn('exchange_rate', response_data)
        self.assertEqual(response_data['exchange_rate'], 0.85)

    def test_get_invalid_exchange_rate(self):
        """
        Test that the API returns 404 when an exchange rate for an invalid currency pair is requested.
        """
        response = self.client.get(reverse('get_exchange_rate', kwargs={'base': 'USD', 'quote': 'GBP'}))
        self.assertEqual(response.status_code, 404)

    def test_get_currency_pair_not_found(self):
        """
        Test that the API returns 404 when a non-existent currency pair is requested.
        """
        response = self.client.get(reverse('get_currency_pairs', kwargs={'currency': 'XYZ'}))
        self.assertEqual(response.status_code, 404)
