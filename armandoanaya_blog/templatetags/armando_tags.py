from django import template
from blog.models import BlogCategory
import math

register = template.Library()


@register.inclusion_tag('inclusion_tags/sidebar.html')
def sidebar_widgets():
    categories = list(BlogCategory.objects.all())
    size = math.ceil(len(categories) / 2)

    return {
        'categories_column_1': categories[:size],
        'categories_column_2': categories[size:],
    }
