from django.urls import path
from . import views
 
urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('registro/', views.UserRegistroView.as_view(), name='registro'),
]
 