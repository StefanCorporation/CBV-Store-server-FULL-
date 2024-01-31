from django.contrib import admin
from products.models import Basket, Product, ProductCategory

# Register your models here.
admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_price', 'product_quantity', 'category']
    fields = [
        'product_name', 
        'description', 
        'product_price', 
        'product_quantity', 
        'product_image', 
        'category',
        'created_at'
    ]
    search_fields = ['product_name']
    ordering = ['product_name']


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ['product', 'quantity', 'created_timestamp']
    readonly_fields = ['created_timestamp']
    extra = 0