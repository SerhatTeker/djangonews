from django import template

register = template.Library()

from digests.forms import get_subscription_form

@register.inclusion_tag('digests/_subscription_form_tag.html')
def digests_subscription_form(user, **kwargs):
    form = get_subscription_form(user)
    return {'subscription_form': form}
