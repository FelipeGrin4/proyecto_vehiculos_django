from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls   import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin 
from django.shortcuts import redirect
from django.contrib import messages

from .models import Vehiculo

# Create your views here.

class VehiculoView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Vehiculo
    template_name = "vehiculos/list_vehiculo.html"
    context_object_name = 'list_vehiculos'
   
    permission_required = 'vehiculos.view_vehiculo'
   
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "Usted no tiene permisos para acceder a la vista.")
            return redirect("login")
       
        else:
            messages.info(self.request, "Para continuar, por favor inicie sesión.")
            return redirect("login")



class VehiculoCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Vehiculo
    template_name = "vehiculos/create_vehiculo.html"
    fields = ['marca', 'modelo', 'serial_carroceria', 'serial_motor', 'categoria', 'precio']
    success_url = reverse_lazy('create_vehiculos')
    permission_required = 'add_vehiculomodel'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, "Usted no tiene permisos para acceder a la vista.")
            return redirect("login")
       
        else:
            messages.info(self.request, "Para continuar, por favor inicie sesión.")
            return redirect("login")