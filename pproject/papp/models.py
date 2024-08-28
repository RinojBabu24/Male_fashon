from django.db import models
from django.contrib.auth.models import User
# from papp.models import Product

# Create your models here.

class Category(models.Model):
    slug=models.CharField(max_length=50,null=False,blank=False)
    name=models.CharField(max_length=50,null=False,blank=False)
    # image=models.ImageField(upload_to="images",null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    def __str__(self):
        return self.name
    

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.CharField(max_length=100,null=False,blank=False)
    name=models.CharField(max_length=100,null=False,blank=False)
    product_image=models.ImageField(upload_to="images",null=False,blank=False)
    description=models.CharField(max_length=500,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    orginal_price=models.FloatField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,1=Hidden")
    trending=models.BooleanField(default=False,help_text="0=default,1=Trending")

    def __str__(self):
        return self.name
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Cart {self.id} (User: {self.user.username})"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10, blank=True, null=True, default='')  
    def total_price(self):
        return self.product.selling_price * self.quantity

    def __str__(self):
        return f"{self.product.name} (Cart: {self.cart.id})"











    
# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=1)
    
#     def __str__(self):
#         return f"{self.product.name} (User: {self.user.username})"
    
#     def total_price(self):
#         return self.product.selling_price * self.quantity
