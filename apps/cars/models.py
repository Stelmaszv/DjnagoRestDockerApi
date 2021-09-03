from django.db import models

# Create your models here.
class Rate(models.Model):
    id = models.AutoField(primary_key=True)
    rating     = models.IntegerField(null=True)
    car_id     = models.ForeignKey(
        to='cars.Car',
        on_delete=models.CASCADE,
        related_name='car',null=True
    )

class Car(models.Model):
    id           = models.AutoField(primary_key=True)
    make         = models.CharField(max_length=100)
    model        = models.CharField(max_length=100)
    rates_number = models.IntegerField(default=1,null=False)
    avg_rating   = models.FloatField(default=1)
    rates = models.ManyToManyField(to='cars.Rate', related_name='rates')