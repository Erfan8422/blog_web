import datetime

from django import template

register = template.Library()


@register.filter
def mytrucate(value, arg):
    return (value[:arg] + "...")


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)



@register.inclusion_tag("result.html")
def show_result(queryset):
    return {"objects": queryset}