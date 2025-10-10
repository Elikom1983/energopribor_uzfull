from django import template
from django.utils.translation import gettext_lazy as _


register = template.Library()

@register.filter
def upper_text(value):
    return value.upper()
# templatetags/custom_filters.py




register = template.Library()

@register.filter
def price_format(value, currency=None):
    try:
        formatted = f"{int(value):,}".replace(",", " ")  # ҳар 3 рақамдан бир пробел
        if not currency:
            # Агар валюта берилмаган бўлса, таржима қилинади
            currency = _("сум")  # русча сайтда "сум"га таржима қилинади
        return f"{formatted} {currency}"
    except:
        return value
