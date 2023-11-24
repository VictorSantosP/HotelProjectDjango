from django import forms
from trivagoHotel.models import Hotel

class HotelModelForm(forms.ModelForm):

    class Meta:
        model = Hotel
        fields = '__all__'



