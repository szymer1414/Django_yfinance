from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from .models import Currency, ExchangeRate
from django.http import HttpResponse
# Create your views here.
def get_currencies(request):
    #return HttpResponse("<h1>Currency page!</h1>")
    currencies = Currency.objects.all()
    result = [{"code": c.code} for c in currencies]
    #return render(request, result)
    return JsonResponse(result, safe=False)

def get_exchange_rate(request, base, quote):
     #return HttpResponse("<h1>get_exchange_rat</h1>")
     
    pair = f"{base}{quote}"
    rate = ExchangeRate.objects.filter(currency_pair=pair).first()
    result = {
            "currency_pair": rate.currency_pair,
            "exchange_rate": rate.exchange_rate
    }
    return (result)
def load_data(request):
    #return HttpResponse("<h1>load_data</h1>")
    if request.method == 'GET':  # Use GET to fetch and display data
        # at least EURUSD, USDJPY, PLNUSD.
        pairs = ['EURUSD=X', 'USDJPY=X', 'PLNUSD=X', 'EURPLN=X','JPYPLN=X']
        currencies = set()
        currency_data = {}


        for pair in pairs:
            ticker = yf.Ticker(pair)
            info = ticker.history(period="1d")  
            if not info.empty:
                last_price = info['Close'].iloc[-1]
                currency_data[pair] = last_price
            else:
                currency_data[pair] = "Data unavailable"


            clean_pair = pair.replace('=X', '')
            head = clean_pair[:3]
            tail = clean_pair[3:]
            #if head != tail:  
            currencies.add(head)
            currencies.add(tail)

        for currency_code in currencies:
            Currency.objects.get_or_create(code=currency_code)
            
        for currency_pair, rate in currency_data.items():
            ExchangeRate.objects.get_or_create(currency_pair=currency_pair, exchange_rate=rate)


        # Return the unique list of currencies
        return JsonResponse({"currencies": list(currencies)})

    return JsonResponse({"error": "Invalid request method"}, status=400)


