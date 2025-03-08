from django.urls import path
from . import views

app_name = 'orders'


urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('orders/', views.orders, name='orders'),
	path('order/<int:pk>/', views.order, name='order'),
]
