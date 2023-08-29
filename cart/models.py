from django.db import models
from store.models import ProductModel

# Create your models here.

class CartModel(models.Model):
    cart_id = models.CharField(max_length=200,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.cart_id
    
    
    
class CartItemModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.product)
    
