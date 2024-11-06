from django.urls import path
from . import views  
from .views import Strains

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StrainsSitemap
app_name = 'cannabis_db'











sitemaps = {
	'strains_sitemap':StrainsSitemap,


}






urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('strains/', views.strains, name='strains'),

	path('strains/', Strains.as_view(), name='strains'),

	path('strain/<slug:slug>/', views.strain, name='strain'),
	path('dispensaries/', views.dispensaries, name='dispensaries'),
	path('dispensary/<slug:slug>/', views.dispensary, name='dispensary'),
	path('add_dispensary/', views.add_dispensary, name='add_dispensary'),
	path('remove_dispensary/<int:pk>/', views.remove_dispensary, name='remove_dispensary'),
	path('brands/', views.brands, name='brands'),
	path('brand/<slug:slug>/', views.brand, name='brand'),
	path('process_strain_review/<int:pk>/', views.process_strain_review, name='process_strain_review'),
	path('delete-review-rating/<int:pk>/', views.delete_review_rating, name='delete_review_rating'),
	path('flavors/', views.flavors, name='flavors'),
	path('search-results/', views.search_results, name='search_results'),
	path('flavor/<slug:slug>/', views.flavor, name='flavor'),
	path('like-strain/<int:pk>/', views.like_strain, name='like_strain'),
	path('save-strain/<int:pk>/', views.save_strain, name='save_strain'),
	path('save-dispensary/<int:pk>/', views.save_dispensary, name='save_dispensary'),
	path('dislike-strain/<int:pk>/', views.dislike_strain, name='dislike_strain'),
	path('saved-strains/<int:pk>/', views.saved_strains, name='saved_strains'),
	path('saved-dispensaries/<int:pk>/', views.saved_dispensaries, name='saved_dispensaries'),
	path('maps/', views.maps, name='maps'),
	path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('bookmarks/', views.bookmarks, name='bookmarks'),
	path('add_to_bookmarks/<int:id>/', views.add_to_bookmarks, name='add_to_bookmarks'),
	path('remove-from-bookmarks/<int:id>/', views.remove_from_bookmarks, name='remove_from_bookmarks'),
	path('consumed/<int:pk>/', views.consumed, name='consumed')

]

