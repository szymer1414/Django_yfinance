from django.db import models

# Create your models here.

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)

    def __str__(self):
        return self.code
    
class Currencypair(models.Model):
    pair_code = models.CharField(max_length=6, unique=True)
    base_currency = models.ForeignKey(Currency, related_name='base_currency', on_delete=models.CASCADE)
    quote_currency = models.ForeignKey(Currency, related_name='quote_currency', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pair_code

class ExchangeRate(models.Model):
    currency_pair = models.ForeignKey(Currencypair, on_delete=models.CASCADE)
    exchange_rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.currency_pair} - {self.exchange_rate}"