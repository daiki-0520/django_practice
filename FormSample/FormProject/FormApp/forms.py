from django import forms
from django.core import validators
from .models import Post

def check_name(value):
    if value == 'aaa':
        raise validators.ValidationError('その名前はダメ')
class UserInfo(forms.Form):
    name = forms.CharField(label = '名前', max_length = 10, validators=[check_name])
    age = forms.IntegerField(validators = [validators.MinValueValidator(20, message = '20以上じゃないと駄目だよ')])
    mail = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'mail-class', 'placeholder': 'sample@mail.com'})
    )
    
    is_married = forms.BooleanField()
    birthday = forms.DateField(initial = '1909-9-1')
    salary = forms.DecimalField()
    job = forms.ChoiceField(choices=(
        (1, '正社員'),
        (2, '学生'),
        (3, '無色'),
    ), widget = forms.RadioSelect)
    hobby = forms.MultipleChoiceField(choices=(
        (1, 'スポーツ'),
        (2, 'reading'),
        (3, 'movie')
    ),widget = forms.CheckboxSelectMultiple)
    homepage = forms.URLField()
    memo = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        self.fields['job'].widget.attrs['id'] = 'id_job'
        self.fields['hobby'].widget.attrs['class'] = 'hobbies_class'

    def clean_homepage(self):
        homepage = self.cleaned_data['homepage']
        if not homepage.startswith('https'):
            raise forms.ValidationError('ホームページのURLはhttpsのみだよー')

    #def clean(self):
     #   cleaned_data = super().clean()
      #  mail = cleaned_data['mail']
       # verify_mail = cleaned_data['verify_mail']
        #if mail != verify_mail:
         #   raise forms.ValidationError('メールアドレスが一致してません')


class BaseForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        print(f'Form: {self.__class__.__name__}実行')
        return super(BaseForm, self).save(*args, **kwargs)


class PostModelForm(BaseForm):

    memo = forms.CharField(
        widget=forms.Textarea(attrs = {'rows':30, 'cols':20})
    )

    class Meta:
        model = Post
        fields = '__all__'
    
    def save(self, *args, **kwargs):
        obj = super(PostModelForm, self).save(commit = False, *args, **kwargs)
        obj.name = obj.name.upper()
        obj.save()
        return obj