from django.forms import ModelForm, Textarea, TextInput, EmailInput
from .models import *

class SupportForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        
        labels = {
            'name': 'Имя:',
            'email': 'Электроная почта:',
            'message': 'Ваше сообщение:',
        }

        widgets = {
            'name': TextInput(attrs={'placeholder': 'Введите имя...'}),
            'email': EmailInput(attrs={'placeholder': 'Введите свою почту...'}),
            'message': Textarea(attrs={'cols': 60, 'rows': 10,
                                       'placeholder': 'Введите сюда свое сообщение...'}),
        }

    # Добавил class="form-control" для каждого элемента input
    def __init__(self, *args, **kwargs):
        super(SupportForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
