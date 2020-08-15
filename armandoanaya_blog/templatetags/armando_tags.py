from django import template
from django.conf import settings
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


@register.inclusion_tag('inclusion_tags/google_analytics.html')
def google_analytics():
    google_analytics_id = settings.GOOGLE_ANALYTICS_ID

    return {
        'google_analytics_id': google_analytics_id
    }
