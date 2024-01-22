from django.urls import path
from . import views 
from .forms import LoginForm
from django.contrib.auth import views as auth_views



app_name = 'accounts'

urlpatterns = [
    path('', views.front_page, name='front_page'),
    path('create-account/', views.create_account, name='create_account'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', form_class=LoginForm), name="login"),

]