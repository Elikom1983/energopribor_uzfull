from django import forms
from .models import Order
from django.core.exceptions import ValidationError
from parler.forms import TranslatableModelForm
from django import forms
from dal import autocomplete
from .models import AttributeValue

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address_line', 'email',  'phone', 'message']






class ProductAttributeValueForm(TranslatableModelForm):
    value = forms.ModelChoiceField(
        label="Qiymat (Value)",
        queryset=AttributeValue.objects.all(),
        widget=autocomplete.ModelSelect2(
            url='store:attribute-values-autocomplete',
            attrs={
                'data-placeholder': 'Qiymatni tanlang yoki yozing',
                'data-tags': 'true',          # yangi yozish imkonini beradi
                'data-allow-clear': 'true',
            }
        )
    )

    class Meta:
        model = AttributeValue
        fields = ['attribute', 'value']