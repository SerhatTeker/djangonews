from django import template

register = template.Library()

from digest.forms import get_subscription_form

@register.inclusion_tag('digest/_subscription_form_tag.html')
def digest_subscription_form(user, **kwargs):
    form = get_subscription_form(user)
    return {'subscription_form': form}
