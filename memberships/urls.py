from django.urls import path
from . import views  
from .views import PublicProfile, PasswordChangeView,ChangePassView
from django.contrib.auth import views as auth_views
app_name = 'memberships'

urlpatterns = [
	path('', views.profile, name='profile'),
	path('edit_profile/<int:pk>/', views.edit_profile, name='edit_profile'),
	path('delete_profile/<int:pk>/', views.delete_profile, name='delete_profile'),
	path('follow-profile/<int:pk>/', views.follow_profile, name='follow_profile'),
	path('public-profile/<int:pk>/', PublicProfile.as_view(), name='public_profile'),
	path('follow-user/<int:pk>/', views.follow_user, name='follow_user'),
	path('unfollow-user/<int:pk>/', views.unfollow_user, name='unfollow_user'),
	path('submit-strain/<int:pk>/', views.submit_strain, name='submit_strain'),
	path('my-strains/<int:pk>/', views.my_strains, name='my_strains'),

	#path('settings/<int:pk>/', views.settings, name='settings'),
	
	path('password/', ChangePassView.as_view(template_name='memberships/settings.html'), name='settings'),

	

	

]
