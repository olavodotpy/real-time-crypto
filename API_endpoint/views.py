from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .utils import APIHandler





class Bitcoin(APIView):

    def get(self, request):

        # Calls the API with the symbol and path value retrieved from POST
        handler = APIHandler("https://api.binance.us/api/v3")

        handler.set_path = "ticker/price"

        # Gets the JSON response    
        data = handler.json_requests_response({"symbol": "BTCUSDT"})

        return Response(data, status=status.HTTP_200_OK)



class Ethereum(APIView):

    def get(self, request):

        handler = APIHandler("https://api.binance.us/api/v3")

        handler.set_path = "ticker/price"

        # Gets the JSON response
        data = handler.json_requests_response({"symbol": "ETHUSDT"})

        return Response(data, status=status.HTTP_200_OK)



class String_Bitcoin(APIView):

    pass




class String_Ethereum(APIView):

    pass
