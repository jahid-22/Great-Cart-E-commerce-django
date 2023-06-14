from django.contrib import admin
from . models import Catagory

# Register your models here.
class AdminCatagory(admin.ModelAdmin):
    prepopulated_fields = {'slug':('catagory_name',)}
    list_display = ['id','catagory_name', 'slug']


admin.site.register(Catagory,AdminCatagory)