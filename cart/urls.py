from django.urls import path
from . import views

app_name = 'cart'


urlpatterns = [

	path('', views.front_page, name='front_page'),
	
	path('cart/<int:pk>/', views.cart, name='cart'),

	path('add-product-to-cart/<int:pk>/', views.add_product_to_cart, name='add_product_to_cart'),
	path('update-product-in-cart/<int:pk>/', views.update_product_in_cart, name='update_product_in_cart'),
	path('delete-product-from-cart/<int:pk>/', views.delete_product_from_cart, name='delete_product_from_cart'),

	
]
