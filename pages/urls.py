from django.urls import path, include
from . import views





urlpatterns = [ 
    path('', views.bitcoin_page, name='bitcoin_page'),
    path('ethereum/', views.ethereum_page, name='ethereum_page'),
]