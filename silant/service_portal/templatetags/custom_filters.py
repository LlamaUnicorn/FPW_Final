from django import template

register = template.Library()


@register.filter()
def serial_number(value):
    pass