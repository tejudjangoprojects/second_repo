from django import template
register=template.Library()

#register.filter('f8',first_eight_upper)
@register.filter(name='f8')
def first_eight_upper(value,arg):
    result=value[:4].lower()+str(arg)
    return result
