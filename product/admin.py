from django.contrib import admin

# Register your models here.
from product.models import Product,Category


@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ('name', 'description', 'weight', 'active', 'price','category')
    list_filter = ('name', 'description', 'weight', 'active', 'price','category')
    search_fields = ('name', 'description', 'weight', 'active', 'price','category')

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('name', 'description')
    list_filter = ('name', 'description')
    search_fields = ('name', 'description')