from django.contrib import admin
from .models import PublicationFiles,VestnikFiles,Pages, Profile
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

admin.site.register(Profile)

class PagesAdminForm(forms.ModelForm):
    content = forms.CharField(label="Desc", widget=CKEditorUploadingWidget())
    content_ru = forms.CharField(label="Desc[ru]", widget=CKEditorUploadingWidget())
    content_en = forms.CharField(label="Desc[en]", widget=CKEditorUploadingWidget())
    content_kk = forms.CharField(label="Desc[kk]", widget=CKEditorUploadingWidget())
    class Meta:
        model = Pages
        fields = '__all__'

#class SeriesAdminForm(forms.ModelForm):
#    description = forms.CharField(label="Desc", widget = CKEditorUploadingWidget())
#    description_ru = forms.CharField(label="Desc[ru]", widget = CKEditorUploadingWidget())
#    description_en = forms.CharField(label="Desc[en]", widget=CKEditorUploadingWidget())
#    description_kk = forms.CharField(label="Desc[kk]", widget=CKEditorUploadingWidget())
#    class Meta:
#        model = Series
#        fields = '__all__'

@admin.register(PublicationFiles)
class PublicationFilesAdmin(admin.ModelAdmin):
    list_display = ('topic','author','soauthor','date','public','archive')
    list_filter = ['author','archive']
    search_fields = ('topic','author','soauthor')
    list_editable = ['archive','public']

    #readonly_fields = ['topic','author','date','soauthor']

#@admin.register(Series)
#class SeriesAdmin(admin.ModelAdmin):
#    list_display = ('name','description')
#    form = SeriesAdminForm

@admin.register(VestnikFiles)
class VestnikFilesAdmin(admin.ModelAdmin):
    list_display = ('name','year')
    list_filter = ['year',]

@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    form = PagesAdminForm