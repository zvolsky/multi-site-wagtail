from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel

class HomePage(Page):
    body = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
