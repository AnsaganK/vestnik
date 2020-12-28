from django import forms
from .models import PublicationFiles,VestnikFiles,Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','full']

class PublicationForm(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('topic','soauthor','file','description')


class VestnikForm(forms.ModelForm):
    class Meta:
        model = VestnikFiles
        fields = ('name', 'file', 'year')


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, label='Логин')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )



class UpdateFormRedactor(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('redactor','reviewer_choice','redactor_return','redactor_return_text','redactor_error','redactor_error_text')


class UpdateFormAntiplagiat(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('antiplagiat','antiplagiat_point','antiplagiat_file')

class UpdateFormReviewers(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('reviewer', 'reviewer_file','reviewer_return','reviewer_return_text','reviewer_error','reviewer_error_text')

class UpdateFormPayloadImg(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('payload_img',)

class UpdateFormPayload(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('payload', 'payload_error', 'payload_error_text')

class UpdateFormProfile(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'full']

class UpdateFormUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class UpdateFileUser(forms.ModelForm):
    class Meta:
        model = PublicationFiles
        fields = ('file',)