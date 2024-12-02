from django.contrib import admin
from .models import Currency, Currencypair, ExchangeRate
# Register your models here.

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('code',)


class ExchangeRateInline(admin.TabularInline):
    model = ExchangeRate
    extra = 0  
    readonly_fields = ['exchange_rate', 'timestamp']  

@admin.register(Currencypair)
class CurrencypairAdmin(admin.ModelAdmin):
    list_display = ('pair_code',)
    search_fields = ('pair_code',)
    inlines = [ExchangeRateInline]  


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency_pair', 'exchange_rate', 'timestamp')
    search_fields = ('currency_pair__pair_code',)