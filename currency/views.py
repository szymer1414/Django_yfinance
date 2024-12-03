from django.http import HttpResponse
import yfinance as yf
from django.http import JsonResponse
from .models import Currency, ExchangeRate,Currencypair
import logging
from django.db.models import Q 

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def get_currencies(request):
    #return HttpResponse("<h1>Currency page!</h1>")
    currencies = Currency.objects.all().order_by('code')
    result = [{"code": c.code} for c in currencies]
    return JsonResponse(result, safe=False)

def get_currency_pairs(request, currency):
    #return HttpResponse("<h1>get_currency_pairs</h1>")
    '''
    currency_pairs2 = ExchangeRate.objects.filter(
        Q(currency_pair__pair_code__startswith=currency) |
        Q(currency_pair__pair_code__endswith=currency))
    related_currencies = set()
    for pair in currency_pairs:
        base_currency = pair.currency_pair.pair_code[:3]
        quote_currency = pair.currency_pair.pair_code[3:]
        
        if base_currency == currency:
            related_currencies.add(quote_currency)
        else:
            related_currencies.add(base_currency)
    '''
    currency_pairs = ExchangeRate.objects.filter(
        Q(currency_pair__base_currency__code=currency) |
        Q(currency_pair__quote_currency__code=currency)
    )
    related_currencies = set()
    
    for rate in currency_pairs:
        pair = rate.currency_pair
        if pair.base_currency.code == currency:
            related_currencies.add(pair.quote_currency.code)
        else:
            related_currencies.add(pair.base_currency.code)

    return JsonResponse({"related_currencies": list(related_currencies)})


def get_exchange_rate(request, base, quote):
    #return HttpResponse("<h1>get_exchange_rat</h1>")
    #search for PLNUSD or USDPLN 
    pair1 = f"{base}{quote}"
    pair2 = f"{quote}{base}" 
    #getting the most recent rate 
    rate = ExchangeRate.objects.filter(
        Q(currency_pair__pair_code=pair1) | Q(currency_pair__pair_code=pair2)).order_by('-timestamp').first()
    if rate:
        if rate.currency_pair.pair_code == pair1:
            result = {
                "currency_pair": rate.currency_pair.pair_code,
                "exchange_rate": rate.exchange_rate,
            }
        else:
            result = {
                "currency_pair": pair1,
                "exchange_rate": (1/rate.exchange_rate),
            }
        return JsonResponse(result)
    return JsonResponse({"error": "Exchange rate not found"}, status=404)
def load_data(request):
    #return HttpResponse("<h1>load_data</h1>")
    if request.method == 'GET': 
        # at least EURUSD, USDJPY, PLNUSD.
        pairs = ['EURUSD=X', 'USDJPY=X', 'PLNUSD=X', 'EURPLN=X','PLNJPY=X','GBPUSD=X','EURGBP=X','EURJPY=X']
        currencies = set() #
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
            currencies.add(clean_pair[:3])
            currencies.add(clean_pair[3:])


        for currency_code in currencies:
            Currency.objects.get_or_create(code=currency_code)
            logger.info(f"Created new Currency: {currency_code}")

        for pair, rate in currency_data.items():
            clean_pair = pair.replace('=X', '')
            base_currency = Currency.objects.get(code=clean_pair[:3])
            quote_currency = Currency.objects.get(code=clean_pair[3:])

            currency_pair, created = Currencypair.objects.get_or_create(
                base_currency=base_currency,
                quote_currency=quote_currency,
                pair_code=clean_pair 
            )
            if created:
                logger.info(f"Created new CurrencyPair: {clean_pair}")
            else:
                logger.info(f"CurrencyPair {clean_pair} already exists")


            ExchangeRate.objects.get_or_create(currency_pair=currency_pair, exchange_rate=rate)
            logger.info(f"Created new ExchangeRate: {clean_pair} with rate {rate}")

        return JsonResponse({"currencies": list(currencies)})
    return JsonResponse({"error": "Invalid request method"}, status=400)


