from django.contrib import admin
from cars.models import Car, Brand



# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo')
    search_fields = ('model','brand__name')

admin.site.register(Car, CarAdmin)