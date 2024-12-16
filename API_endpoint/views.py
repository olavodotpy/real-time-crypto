from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.core.cache import cache




BINANCE_API = "https://api.binance.us/api/v3/ticker/price"
COINGECKO_API = "https://api.coingecko.com/api/v3"


class Bitcoin(APIView):

    def get(self, request):

        param = {"symbol": "BTCUSDT"}

        response = requests.get(BINANCE_API, param)

        data = {
            "price": response.json()['price']
        }

        return Response(data)



class Ethereum(APIView):

    def get(self, request):

        param = {"symbol": "ETHUSDT"}

        response = requests.get(BINANCE_API, param)

        data = {
            "price": response.json()['price']
        }

        return Response(data)



class String_Bitcoin(APIView):

    def get(self, request):

        path = COINGECKO_API + "/coins/bitcoin"

        data = requests.get(path)

        data_cached = cache.get('DATA_BTC')

        if data_cached:
            return Response(data_cached)

        data = {
            "title": data.json()['name'],
            "body": data.json()['description']['en']
        }

        cache.set('DATA_BTC', data, timeout=86400)

        Response(data)



class String_Ethereum(APIView):

    def get(self, request):

        path = COINGECKO_API + "/coins/ethereum"

        data = requests.get(path)

        data_cached = cache.get('DATA_ETH')

        if data_cached:
            return Response(data_cached)

        data = {
            "title": data.json()['name'],
            "body": data.json()['description']['en']
        }

        cache.set('DATA_ETH', data, timeout=86400)

        Response(data)
