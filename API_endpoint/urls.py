from django.urls import path
from . import views




urlpatterns = [
    path('api/vs/price/bitcoin', views.Bitcoin.as_view()),
    path('api/vs/price/ethereum', views.Ethereum.as_view()),
    path('api/vs/bitcoin', views.String_Bitcoin.as_view()),
    path('api/vs/ethereum', views.String_Ethereum.as_view()),
]
