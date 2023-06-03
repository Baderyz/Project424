
from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(
        upload_to='https://fdn2.gsmarena.com/vv/pics/apple/apple-iphone-14-pro-max-1.jpg')

    def str(self):
        return f"{self.name} {self.price} {self.manufacturer} {self.description}"
