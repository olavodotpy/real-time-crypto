from django.shortcuts import render
import requests
import os
import dotenv




dotenv.load_dotenv()

def bitcoin_page(request):
    data = requests.get(os.getenv("PRODUCTION") + "/api/vs/price/bitcoin")

    return render(request, os.getenv("DOC_HTML_BITCOIN"), data.json())


def ethereum_page(request):
    pass
