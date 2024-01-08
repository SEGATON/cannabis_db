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
	path('flavors/', views.flavors, name='flavors'),
	path('flavor/<slug:slug>/', views.flavor, name='flavor'),

	path('like-strain/<int:pk>/', views.like_strain, name='like_strain'),
	path('unlike-strain/<int:pk>/', views.unlike_strain, name='unlike_strain'),

	path('save-strain/<int:pk>/', views.save_strain, name='save_strain'),
	path('unsave-strain/<int:pk>/', views.unsave_strain, name='unsave_strain'),

	path('dislike-strain/<int:pk>/', views.dislike_strain, name='dislike_strain'),
	path('undislike-strain/<int:pk>/', views.undislike_strain, name='undislike_strain'),
	path('saved-strains/<int:pk>/', views.saved_strains, name='saved_strains'),

]

