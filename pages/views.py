from django.shortcuts import render
import requests
import os
import dotenv




dotenv.load_dotenv()

HTML_BITCOIN="bitcoin.html"
HTML_ETHEREUM="ethereum.html"

def bitcoin_page(request):
    data = requests.get(os.getenv("PRODUCTION") + "/api/vs/price/bitcoin")
    data_string = requests.get(os.getenv("PRODUCTION") + "/api/vs/bitcoin")

    context = {
        "price": data.json()['price'],
        "title": data_string.json()['title'],
        "body": data_string.json()['body'],
    }

    return render(request, HTML_BITCOIN, context)


def ethereum_page(request):
    data = requests.get(os.getenv("PRODUCTION") + "/api/vs/price/ethereum")
    data_string = requests.get(os.getenv("PRODUCTION") + "/api/vs/ethereum")

    context = {
        "price": data.json()['price'],
        "title": data_string.json()['title'],
        "body": data_string.json()['body'],
    }

    return render(request, HTML_ETHEREUM, context)
