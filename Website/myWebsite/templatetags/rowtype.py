from django import template

register= template.Library()

@register.simple_tag
def get_type(type=None):
	return type