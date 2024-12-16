from rest_framework.views import APIView
from rest_framework.response import Response
import requests





BINANCE_API = "https://api.binance.us/api/v3/ticker/price"


class Bitcoin(APIView):

    def get(self, request):

        param = {"symbol": "BTCUSDT"}

        response = requests.get(BINANCE_API, param)

        context = {
            "price": response.json()['price']
        }

        return Response(context)



class Ethereum(APIView):

    def get(self, request):

        param = {"symbol": "ETHUSDT"}

        response = requests.get(BINANCE_API, param)

        context = {
            "price": response.json()['price']
        }

        return Response(context)



class String_Bitcoin(APIView):

    pass




class String_Ethereum(APIView):

    pass
