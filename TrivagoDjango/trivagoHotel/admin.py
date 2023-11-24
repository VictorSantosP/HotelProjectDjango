from django.contrib import admin
from trivagoHotel.models import Hotel, Brand



# Register your models here.
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Brand, BrandAdmin)

class HotelAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value', 'photo')
    search_fields = ('model','brand__name')

admin.site.register(Hotel, HotelAdmin)