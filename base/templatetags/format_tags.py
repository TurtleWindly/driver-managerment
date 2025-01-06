from django import template
import re

register = template.Library()


@register.filter
def currency(value):
    """Adding comma to separate number"""
    result = str(value)
    match = re.match(r"-?\d+", result)
    if match:
        prefix = match[0]
        prefix_with_commas = re.sub(r"\d{3}", r"\g<0>,", prefix[::-1])[::-1]
        # Remove a leading comma, if needed.
        prefix_with_commas = re.sub(r"^(-?),", r"\1", prefix_with_commas)
        result = prefix_with_commas + result[len(prefix) :]
    return result


@register.filter
def decimal_value(value):
    return str(value).replace(",", ".")
