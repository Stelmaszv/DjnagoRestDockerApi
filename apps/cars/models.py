from django.db import models
import requests

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
    # for class
    api_url="https://vpic.nhtsa.dot.gov/api/vehicles/getallmakes?format=json"

    # for models
    id           = models.AutoField(primary_key=True)
    make         = models.CharField(max_length=100)
    model        = models.CharField(max_length=100)
    rates_number = models.IntegerField(default=1,null=False)
    avg_rating   = models.FloatField(default=1)
    rates        = models.ManyToManyField(to='cars.Rate', related_name='rates')

    def __init__(self, *args, **kwargs):
        super(Car, self).__init__(*args, **kwargs)
        self.set_avrage_reating()
        self.set_rates_number()

    def set_rates_number(self):
        if self.id is not None:
            self.rates_number = self.rates.count()

    def set_avrage_reating(self):
        if self.id is not None:
            rote = 0
            for item in self.rates.all():
                rote = rote + item.rating
            if self.rates.count() > 0:
                self.avg_rating = rote / self.rates.count()

    def delete(self, *args, **kwargs):
        for rate in self.rates.all():
            rate.delete()
        super(Car, self).delete(*args, **kwargs)

    def get_JSON(self):
        response = requests.get(self.api_url)
        return response.json()['Results']

    def save(self, *args, **kwargs):
        data=self.get_JSON()
        found = False
        for car in data:
            if car['Make_Name'] == self.make:
                found = True
        if found is False:
            raise ValueError("Car doesn't exist !")
        super(Car, self).save(*args, **kwargs)

    def __str__(self):
        return self.make