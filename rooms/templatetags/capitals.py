from django import template

register = template.Library()


@register.filter()
def capitals(value):
    return value.capitalize()
