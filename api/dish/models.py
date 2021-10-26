from django.db import models

# Create your models here.


class Dish(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    previous_price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=False)

    image = models.ImageField(upload_to='images/', null=True, blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
