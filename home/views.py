from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from django.views.decorators.csrf import csrf_exempt

import requests

from .utils import APIHandler





def home_view(request):
    print('teste log')
    return render(request, 'home/home.html')



def ethereum_view(request):
    print('teste log')
    return render(request, 'home/pageEthereum.html')




class PriceViewBitcoin(APIView):

    @csrf_exempt
    def get(self, request):

        print("Tentando acessar a API da Binance...")
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT")
        print(f"Status code: {response.status_code}")
        print(f"Response body: {response.text}")

        # Calls the API with the symbol and path value retrieved from POST
        handler = APIHandler("https://api.binance.com/api/v3")

        handler.set_path = "ticker/price"

        # Gets the JSON response    
        data = handler.json_requests_response({"symbol": "BTCUSDT"})

        return Response(data, status=status.HTTP_200_OK)




class PriceViewEthereum(APIView):
    
    @csrf_exempt
    def post(self, request):

        print("chegou no POST")

        data = request.data
        path = data.get("path_binance")
        symbol = data.get("symbol")

        # save to session
        if request.session.get('symbol') != symbol or request.session.get('path_binance') != path:
            request.session['symbol'] = symbol
            request.session['path_binance'] = path

        return Response({"message": f"data received: {path}, {symbol}"})


    @csrf_exempt
    def get(self, request):

        print("Tentando acessar a API da Binance...")
        response = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT")
        print(f"Status code: {response.status_code}")
        print(f"Response body: {response.text}")

        path = request.session.get('path_binance')
        symbol = request.session.get('symbol')

        if not path or not symbol:
        # Returns a more detailed response
            return Response(
                {"error": "Path or symbol is missing in session data."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Calls the API with the symbol and path value retrieved from POST
        handler = APIHandler("https://api.binance.com/api/v3")

        handler.set_path = path

        # Gets the JSON response
        data = handler.json_requests_response({"symbol": f"{symbol}"})

        return Response(data, status=status.HTTP_200_OK)