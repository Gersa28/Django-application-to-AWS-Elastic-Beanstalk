from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Order
from .forms import OrderProductForm


class MyOrderView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/my_order.html"
    context_object_name = "order" # Sino lo especificamos Django asignará uno automáticamente, con este "order" podremor accederlo desde el Django Template

    # https://ccbv.co.uk/
    def get_object(self, queryset=None):
        return Order.objects.filter(is_active=True, user=self.request.user).first()
        # Filter devuelve una lista, para que sea un elemento debemos colocar first()


class CreateOrderProductView(LoginRequiredMixin, CreateView):
    template_name = "orders/create_order_product.html"
    form_class = OrderProductForm
    # success_url = reverse_lazy("my_order")
    success_url = reverse_lazy("list_product")

    def form_valid(self, form): # Si el submit del formulario es válido entonces :
        order, _ = Order.objects.get_or_create( # Si no encuentra una orden en curso la crea
            is_active=True,
            user=self.request.user,
        )
        form.instance.order = order
        form.instance.quantity = 1
        form.save()
        return super().form_valid(form)
