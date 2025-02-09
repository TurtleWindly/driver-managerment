from django import template

register = template.Library()


@register.filter
def vars(obj):
    return obj.__dict__
