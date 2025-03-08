from django.urls import path
from . import views

app_name = 'addresses'


urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('addresses/', views.addresses, name='addresses'),
	path('address/<int:pk>/', views.address, name='address'),
]
