from django import template

register = template.Library()


# @register.filter
# def get_item(dictionary, key):
#     return dictionary.get(key)
@register.filter
def get_item(dictionary, key):
    if isinstance(dictionary, dict):
        return dictionary.get(key)
    else:
        print(f"Warning: depuis votre repertoire templatetags et votre fonction custom_filters vous faites un get key '{
              key}' sur un ojbet qui n'est pas un dictionnaire '{dictionary}'.")
        return None
