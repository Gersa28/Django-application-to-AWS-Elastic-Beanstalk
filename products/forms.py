from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Nombre")
    description = forms.CharField(max_length=300, label="Descripción")
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Precio")
    available = forms.BooleanField(initial=True, label="Disponible", required=False)
    photo = forms.ImageField(label="Foto", required=False)

    def save(self):
        # cleaned_data es un diccionario que contiene los datos del formulario
        # después de que han pasado por las validaciones de cada campo.
        # Es seguro acceder a estos datos, ya que Django se asegura de que sean válidos.
        Product.objects.create(
            # Aquí se accede al valor del campo "name" desde cleaned_data
            name=self.cleaned_data["name"],
            # Se accede al valor del campo "description"
            description=self.cleaned_data["description"],
            # Se accede al valor del campo "price"
            price=self.cleaned_data["price"],
            # Se accede al valor del campo "available"
            available=self.cleaned_data["available"],
            # Se accede al valor del campo "photo"
            photo=self.cleaned_data["photo"],
        )
        # Este método crea y guarda un nuevo objeto Product en la base de datos
        # usando los datos validados del formulario.
