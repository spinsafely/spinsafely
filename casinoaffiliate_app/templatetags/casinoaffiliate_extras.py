from django import template

register = template.Library()

@register.filter
def rating(value):
    return (100 * value) / 5