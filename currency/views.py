from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from .models import Currency, ExchangeRate
from django.http import HttpResponse
# Create your views here.
def get_currencies(request):
     return HttpResponse("<h1>Welcome to the Home Page!</h1>")
     '''currencies = Currency.objects.all()
    result = [{"code": c.code} for c in currencies]
    return render(request, result)'''

def get_exchange_rate(request, base, quote):
     return HttpResponse("<h1>get_exchange_rat</h1>")
     '''
    pair = f"{base}{quote}"
    rate = ExchangeRate.objects.filter(currency_pair=pair).first()
    result = {
            "currency_pair": rate.currency_pair,
            "exchange_rate": rate.exchange_rate
    }
    return (result)'''
def load_data(request):
    return HttpResponse("<h1>load_data</h1>")
    '''if request.method == 'POST':
        pairs = ['EURUSD=X', 'USDJPY=X', 'PLNUSD=X']
        for pair in pairs:
            ticker = yf.Ticker(pair)
            info = ticker.history(period="1d")
            if not info.empty:
                last_price = info['Close'].iloc[-1]
                base, quote = pair.split("USD=X")[0], "USD"
                currency_pair = base + quote
                
                # Add currencies to Currency table
                Currency.objects.get_or_create(code=base)
                Currency.objects.get_or_create(code=quote)

                # Add exchange rate to ExchangeRate table
                ExchangeRate.objects.create(currency_pair=currency_pair, exchange_rate=last_price)
        return JsonResponse({"message": "Data loaded successfully"})
    return JsonResponse({"error": "Invalid request"}, status=400)
'''