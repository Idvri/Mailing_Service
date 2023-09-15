from django import forms

from service.models import Mailing, Client


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'clients':
                continue
            else:
                field.widget.attrs['class'] = 'form-control'


class CreateMailingForm(StyleFormMixin, forms.ModelForm):
    mailing_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }
        ),
        label='Дата и время рассылки'
    )

    clients = forms.ModelMultipleChoiceField(
        queryset=Client.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Клиенты'
    )

    mail_theme = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Введите текст'}),
        label='Тема сообщения'
    )

    mail_text = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Введите текст'}),
        label='Текст сообщения'
    )

    class Meta:
        model = Mailing
        exclude = ('status',)


class UpdateMailingForm(StyleFormMixin, forms.ModelForm):
    mailing_time = forms.DateTimeField(
        widget=forms.DateTimeInput(
            attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }
        ),
        label='Дата и время рассылки'
    )

    clients = forms.ModelMultipleChoiceField(
        queryset=Client.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Клиенты'
    )

    class Meta:
        model = Mailing
        fields = ('mailing_time', 'regularity', 'clients')