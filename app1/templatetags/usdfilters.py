from django import template

register=template.Library()

def count(value,arg):
    c=0
    for i in range(len(value)):
        if value[i:i+len(arg)]==arg:
            c+=1
    return c
register.filter('count',count)

def swap(value):
    return value.swapcase()
register.filter('swap',swap)

def upper(value):
    return value.upper()
register.filter('upper',upper)

# DECORATED FILTERS
@register.filter() # if you not provide an argument it will take your function name as argument
def lower(value):
    return value.lower()

