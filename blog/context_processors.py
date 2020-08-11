from django.conf import settings


def disqus_settings(request):
    return {
        'DISQUS_PAGE_URL': settings.DISQUS_PAGE_URL,
        'DISQUS_PAGE_IDENTIFIER': settings.DISQUS_PAGE_IDENTIFIER,
    }
