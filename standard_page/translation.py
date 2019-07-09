from .models import StandardPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(StandardPage)
class StandardPageTR(TranslationOptions):
    fields = (
        'body',
    )
