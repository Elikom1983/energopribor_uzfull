from django import template

register = template.Library()

@register.filter
def upper_text(value):
    return value.upper()
