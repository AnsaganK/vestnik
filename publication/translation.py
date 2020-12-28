from modeltranslation.translator import TranslationOptions,register
from .models import PublicationFiles,Pages

#@register(Series)
#class SeriesTranslationOptions(TranslationOptions):
#    fields = ('name','description')

@register(Pages)
class PagesTranslationoptions(TranslationOptions):
    fields = ('title','content')