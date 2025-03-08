from django.urls import path
from . import views

app_name = 'vendors'


urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('vendors/', views.vendors, name='vendors'),
	path('vendor/<slug:slug>/', views.vendor, name='vendor'),
	path('dashboard/<int:pk>/', views.dashboard, name='dashboard'),
]
