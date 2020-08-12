from django import template

# from djangonews.digests.forms import get_subscription_form
from ..forms import get_subscription_form

register = template.Library()


@register.inclusion_tag("digests/_subscription_form_tag.html")
def digests_subscription_form(user, **kwargs):
    form = get_subscription_form(user)
    return {"subscription_form": form}
