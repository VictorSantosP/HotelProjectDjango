from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarModelForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from typing import Any

# Create your views here.


@method_decorator(login_required(login_url='login'), name='dispatch')
class newCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class carsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'


    def get_queryset(self):
        cars = super().get_queryset().order_by('model') 
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains = search)
        return cars


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    #context_object_name = 'cars'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'



                  


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
