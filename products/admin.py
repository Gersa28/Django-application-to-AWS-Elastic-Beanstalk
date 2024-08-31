from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ["name", "price"]
    search_fields = ["name"] # Filtros de búsqueda


admin.site.register(Product, ProductAdmin) # Parámetros: El Modelo y su Clase Registradora
