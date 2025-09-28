from django import template
from django import template

register = template.Library()

@register.filter
def upper_text(value):
    return value.upper()
# templatetags/custom_filters.py




register = template.Library()

@register.filter
def price_format(value, currency="so'm"):
    try:
        # intcomma ёрдамида ҳар 3 рақамдан бир `'` қўямиз
        formatted = f"{int(value):,}".replace(",", "'")
        return f"{formatted} {currency}"
    except:
        return value

