from django.shortcuts import render
from firstapp.models import Vehicle
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView , DeleteView
from django.urls import reverse_lazy
# Create your views here.
class VehicleListView(ListView):
    model = Vehicle

class VehicleDetailView(DetailView):
    model = Vehicle

class VehicleCreateView(CreateView):
    model = Vehicle
    fields = ['vehicle_number', 'vehicle_type' , 'vehicle_model' , 'vehicle_description']
class VehicleUpdateView(UpdateView):
    model = Vehicle
    fields = ['vehicle_number' ,'vehicle_model' ,'vehicle_description']
    success_url = reverse_lazy('vehicle_list')

class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy('vehicle')
