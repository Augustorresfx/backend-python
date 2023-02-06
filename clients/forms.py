from django.forms import ModelForm
from .models import Product


class ClientForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'discount', ]