from django import forms


class UserInfo(forms.Form):
    name = forms.CharField(label = '名前', max_length = 10)
    age = forms.IntegerField()
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
    fomepage = forms.URLField()
    memo = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(UserInfo, self).__init__(*args, **kwargs)
        self.fields['job'].widget.attrs['id'] = 'id_job'
        self.fields['hobby'].widget.attrs['class'] = 'hobbies_class'