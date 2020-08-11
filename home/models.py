from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    header_image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, null=True
    )
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('header_image'),
        FieldPanel('body', classname="full"),
    ]
