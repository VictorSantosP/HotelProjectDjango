from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from trivagoHotel.models import Hotel
from trivagoHotel.forms import HotelModelForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from typing import Any





class newHotelCreateView(CreateView):
    model = Hotel
    form_class = HotelModelForm
    template_name = 'new_room.html'
    success_url = '/hotels/'


class hotelsListView(ListView):
    model = Hotel
    template_name = 'hotels.html'
    context_object_name = 'trivagoHotel'


    def get_queryset(self):
        cars = super().get_queryset().order_by('model') 
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains = search)
        return cars


class HotelDetailView(DetailView):
    model = Hotel
    template_name = 'room_detail.html'


class HotelUpdateView(UpdateView):
    model = Hotel
    form_class = HotelModelForm
    template_name = 'room_update.html'
    success_url = '/hotels/'
    
class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'room_delete.html'
    success_url = '/hotels/'


class HotelAboutView(DetailView):
    model = Hotel
    template_name = '/about_us.html/'