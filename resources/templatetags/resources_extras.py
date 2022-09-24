from django import template

register = template.Library()

@register.simple_tag
def findage(dob):
    [date, month, year] = dob.split('/')
    return 2022 - int(year)