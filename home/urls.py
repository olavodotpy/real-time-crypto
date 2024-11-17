from django.urls import path

from . import views




urlpatterns = [
    path('', views.home_view, name='bitcoin'),
    path('ethereum/', views.ethereum_view, name='ethereum'),
    path('api/bitcoin/price/', views.PriceViewBitcoin.as_view(), name='get_price_bitcoin'),
    path('api/ethereum/price/', views.PriceViewEthereum.as_view(), name='get_price_ethereum'),
]
