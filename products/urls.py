from .views import ProductFormView, ProductListView, ProductListAPI
from django.urls import path


urlpatterns = [
    path("", ProductListView.as_view(), name="list_product"),
    path("api/", ProductListAPI.as_view(), name="list_product_api"),
    path("agregar/", ProductFormView.as_view(), name="add_new_product"),
]

# http://127.0.0.1:8000/productos/api/
