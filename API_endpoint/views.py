from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests





BINANCE_API = "https://api.binance.us/api/v3/ticker/price"


class Bitcoin(APIView):

    def get(self, request):

        # Calls the API with the symbol and path value retrieved from POST

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

        price = response.json()['price']

        return Response({"price": f"{price}"})



class String_Bitcoin(APIView):

    pass




class String_Ethereum(APIView):

    pass
