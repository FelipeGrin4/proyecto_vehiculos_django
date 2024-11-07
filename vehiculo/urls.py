from django.urls import path
from . import views
 
urlpatterns = [
    path('list/', views.VehiculoView.as_view(), name='list_vehiculos'),
    path('add/', views.VehiculoCreateView.as_view(), name='create_vehiculos')
]
 