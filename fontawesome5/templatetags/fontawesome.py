from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.utils.html import format_html, mark_safe, conditional_escape

from ..app_settings import get_css, get_icon_class


css = get_css()
Icon = get_icon_class()
register = template.Library()


@register.simple_tag
def fa5_icon(*args, **kwargs):
    return Icon(*args, **kwargs).as_html()


@register.simple_tag
def fontawesome5_static():
    staticfiles = []

    for stylesheet in css:
        staticfiles.append(format_html(
            '<link href="{}" rel="stylesheet" media="all">', stylesheet))

    staticfiles.append(format_html(
        '<script type="text/javascript" src="{}"></script>', static('django-fontawesome.js')
    ))

    return mark_safe(conditional_escape('\n').join(staticfiles))
