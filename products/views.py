from django.urls import reverse_lazy
from django.views import generic
from rest_framework.views import APIView
from rest_framework.response import Response

from products.models import Product
from .forms import ProductForm
from .serializers import ProductSerializer

class ProductFormView(generic.FormView):
    form_class = ProductForm    
    template_name = "products/add_product.html"
    success_url = reverse_lazy("add_product")

    def form_valid(self, form): # Recibe el Objeto Formulario y Ejecuta su función save()
        form.save()
        return super().form_valid(form)

class ProductListView(generic.ListView): # Hereda de Vista Genérica
    model = Product
    template_name = "products/list_product.html"
    context_object_name = "products"

class ProductListAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)