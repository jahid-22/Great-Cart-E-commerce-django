from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name','price', 'stock','catagory','created_date','slug', 'modified_date', 'is_available']
    prepopulated_fields = {'slug':('product_name',)}
