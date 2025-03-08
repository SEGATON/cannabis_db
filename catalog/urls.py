from django.urls import path
from . import views

app_name = 'catalog'


urlpatterns = [
	path('', views.catalog, name='catalog'),
	path('front_page/', views.front_page, name='front_page'),
	path('category/<slug:slug>/', views.category, name='category'),

	path('products/', views.products, name='products'),
	path('product/<slug:slug>/', views.product, name='product'),



	path('sort-by/', views.sort_by, name='sort_by'),
]
