from django.db import models

# Create your models here.

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='hotel_brand')
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='trivagoHotel/', blank=True, null=True)

    def __str__(self):
        return self.model

