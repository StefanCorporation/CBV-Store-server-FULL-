from django.db import models
from django.utils import timezone

from users.models import User


# Create your models here.
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=256, unique=True)
    category_description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.category_name



class Product(models.Model):
    product_name = models.CharField(max_length=256, unique=True)
    description = models.TextField(null=True, blank=True)
    product_image = models.ImageField(upload_to='product_images')
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    product_quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return f"Продукт: {self.product_name} | Категория: {self.category.category_name}"
    
    


# обработка колличества использование в контексте
class BasketQuerySet(models.QuerySet):

    def total_sum(self): 
        return sum(basket.sum() for basket in self)
    

    def total_quantity(self):
        return sum(basket.quantity for basket in self)    


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)


    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f"Корзина для {self.user.username} | Продукт: {self.product.product_name}"
    

    def sum(self):
        return self.product.product_price * self.quantity
    


    
