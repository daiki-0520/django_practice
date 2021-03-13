from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

user = get_user_model() #現在作成しているユーザーが買える

class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label = "password", widget = forms.PasswordInput)
    confirm_password = forms.CharField(label = "パスワードさいにゅ力", widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','email', ' password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise ValidationError('パスワードが一致しません')

    def save(self):
        user = super().save(commit = False)
        user.set_password(self.cleaned_data.get('password'))
        user.save()
        return user