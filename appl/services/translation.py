from modeltranslation.translator import register, TranslationOptions

from appl.services.models import MetaData


@register(MetaData)
class MetaDataTranslation(TranslationOptions):
    fields = ('title', 'description', 'h1', )