from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from trivagoHotel.models import Hotel
from trivagoHotel.forms import HotelModelForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from typing import Any

# Create your views here.


@method_decorator(login_required(login_url='login'), name='dispatch')
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

@method_decorator(login_required(login_url='login'), name='dispatch')
class HotelUpdateView(UpdateView):
    model = Hotel
    form_class = HotelModelForm
    template_name = 'room_update.html'
    success_url = '/hotels/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class HotelDeleteView(DeleteView):
    model = Hotel
    template_name = 'room_delete.html'
    success_url = '/hotels/'



                  


"""
--- View de criação de objetos (cadastro) - antiga
def new_car_view(request):
    new_car_form = CarModelForm()

    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        #print(new_car_form.data)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')

    
    return render(request, 
                  'new_car.html',
                  {'new_car_form': new_car_form})
                  
--- View de listagem de objetos - antiga                 
def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('search')
    
    if search:
        cars = Car.objects.filter(brand__name__icontains = search)

    return render(request, 
                  'cars.html',
                  {'cars': cars})
                  
                  
                  
                  """
