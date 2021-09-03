from django.db import models

# Create your models here.
class Rate(models.Model):
    #for class
    mini_rating=0
    max_rating=6

    #for models
    id         = models.AutoField(primary_key=True)
    rating     = models.IntegerField(null=True)
    car_id     = models.ForeignKey(
        to='cars.Car',
        on_delete=models.CASCADE,
        related_name='car',null=True
    )

    def save(self, *args, **kwargs):
        if self.rating > self.mini_rating and self.rating < self.max_rating:
            super(Rate, self).save(*args, **kwargs)
            self.car_id.rates.add(self)
        else:
            raise ValueError("Your rate is " + str(self.rating) + "!  Add a rate for a car from 1 to 5 !")

class Car(models.Model):
    id           = models.AutoField(primary_key=True)
    make         = models.CharField(max_length=100)
    model        = models.CharField(max_length=100)
    rates_number = models.IntegerField(default=1,null=False)
    avg_rating   = models.FloatField(default=1)
    rates        = models.ManyToManyField(to='cars.Rate', related_name='rates')

    def __str__(self):
        return self.make