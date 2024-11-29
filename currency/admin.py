from django.contrib import admin
from .models import Currency, ExchangeRate
# Register your models here.

#admin.site.register(Currency)
#admin.site.register(ExchangeRate)
@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code',)

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency_pair', 'exchange_rate', 'timestamp')