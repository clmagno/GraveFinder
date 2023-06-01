from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={'class': css_class})
@register.filter
def filter_capacity_gt(lots):
    return lots.filter(capacity__gt=0)