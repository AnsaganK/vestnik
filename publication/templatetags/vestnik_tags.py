from django import template

register = template.Library()

@register.filter(name='DateValid')
def markdown_format(number):
    if number:
        if int(number)<10:
            return "0"+str(number)
        else:
            return number
    else:
        return None