from django.db import models
from django.contrib.auth import get_user_model
import string
import random

User = get_user_model()

def create_transaction_id( length=10):
        letters = string.ascii_lowercase
        transaction = ''.join(random.choice(letters) for i in range(length))
        return transaction

# Create your models here.
class Order (models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(default=create_transaction_id, max_length=10)
    #This two methods will update cart total  


    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all() #All orderitems for each product selected
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            if item.product.digital == True:
                shipping = True
        return shipping
    def __str__(self) -> str:
        return self.customer.username