from django.urls import path

from . import views




urlpatterns = [
    path('api/bitcoin/price/', views.PriceViewBitcoin.as_view()),
    path('api/ethereum/price/', views.PriceViewEthereum.as_view()),
]
