from django.db import models
from api.order.models import Order
from api.dish.models import Dish
# Create your models here.


class OrderItem (models.Model):
    dish = models.ForeignKey(
        Dish, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    # This method will update subtotal of each item

    @property
    def get_dish_info(self):
        return {
            'name':self.dish.name,
            'description':self.dish.description,
            'price':self.dish.price,
            'rating':self.dish.rating,
            'image':self.dish.imageURL,
            'dishId':self.dish.pk
        }

    def __str__(self):
        return str(self.dish.name)
