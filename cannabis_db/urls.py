from django.urls import path
from . import views  

app_name = 'cannabis_db'

urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('strains/', views.strains, name='strains'),

	path('strain/<slug:slug>/', views.strain, name='strain'),

	path('brands/', views.brands, name='brands'),
	path('brand/<slug:slug>/', views.brand, name='brand'),
	path('process_strain_review/<int:pk>/', views.process_strain_review, name='process_strain_review'),
	path('delete-review-rating/<int:pk>/', views.delete_review_rating, name='delete_review_rating'),

]

