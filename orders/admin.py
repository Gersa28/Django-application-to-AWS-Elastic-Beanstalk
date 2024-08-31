from django.contrib import admin
from .models import Order, OrderProduct


class OrderProductInlineAdmin(
    admin.TabularInline
):  # Para que aparezcan los productos en la Web Admin
    model = OrderProduct
    extra = 0  # No crea ninguna lñinea extra, solo las que yo creo manualmente


class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInlineAdmin]  # Agregamos el Inline


admin.site.register(Order, OrderAdmin)
