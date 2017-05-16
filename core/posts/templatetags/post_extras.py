from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.templatetags.static import static

from core.classifier.models import Category


register = template.Library()


@register.inclusion_tag('posts/main_menu.html')
def main_menu():
    """
    Creating main page menu.
    :return: rubric roots queryset
    """
    roots = Category.objects.filter(level=0)
    return {'roots': roots}


@register.inclusion_tag('posts/second_menu.html')
def second_menu(parent_slug, current_slug=None):
    parent = Category.objects.get(slug=parent_slug)
    return {'menu_items': parent.get_children(), 'slug': current_slug}


@register.simple_tag
def full_url(url):
    """
    Create full url with hostname.
    :param: absolute url
    :return: full url
    """
    return settings.HOST + url


# ####################    Filters    ################### #

def grouped(l, n):
    # Yield successive n-sized chunks from l.
    for i in range(0, len(l), n):
        yield l[i:i+n]


@register.filter
def group_by(value, arg):
    """
    For grouping iterable items in groups by arg size.
    :param value: iterable,
    :param arg: int
    :return iterator
    """
    return grouped(value, arg)


@register.filter
def times(number):
    """
    For using range function in templatetags.
    :param number: int
    :return range obj:
    """
    return range(1, number+1)


@register.simple_tag
def static_version(path):
    """
    Add version end to static path.
    :param path: path to static file
    :return: full static file path with version
    """
    version = getattr(settings, 'MEDIA_VERSION', '')
    _path = static(path)
    if version:
        _path = '{0}?{1}'.format(_path, version)
    return _path
