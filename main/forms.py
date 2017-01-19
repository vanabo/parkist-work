from django import forms
from geoposition.fields import GeopositionField
from django.forms.extras.widgets import SelectDateWidget
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _

from . models import Order

import datetime

d = datetime.date.today()
s = datetime.datetime.now()
tv1 = s.time
td = datetime.timedelta(minutes=30)
tv = s + td

td2 = datetime.timedelta(days=7)

date1 = d
date2 = d + td2
yy = d.year
dd = d.day
mm = d.month

class Order(ModelForm):
    class Meta:
        model = Order
        fields = ['current_point', 'current_date', 'current_time', 'phone3']
        widgets = {
            'current_date': SelectDateWidget(attrs={'class': 'form-control-date'}),
            'current_time': forms.TimeInput(attrs={'class': 'form-control-time', 'size': '8'}),
            'phone3': forms.TextInput(attrs={'class': 'form-control', 'data-format': '+7 (ddd) ddd-dddd', 'type': 'tel', 'placeholder': 'Введите номер телефона'}),
        }
    class Media:
        css = {
            'all': ('geoposition/css/geoposition.css',),
        }
        js = (
            'geoposition/js/geoposition.js',
        )

    #current_date = forms.DateField(label='Дата*', widget=SelectDateWidget(attrs={'class': 'form-control-date'}),
                                   #initial=d, required=True)
    #current_time = forms.TimeField(label='Время*',
                                   #widget=forms.TimeInput(attrs={'class': 'form-control-time', 'size': '8'}),
                                   #initial=tv, required=True)
    #phone3 = forms.CharField(label='Телефон*', widget=forms.TextInput(
        #attrs={'class': 'form-control', 'placeholder': 'Введите номер телефона'}), required=True)

    #def __init__(self, *args, **kwargs):
        #super(Order, self).__init__(self, *args, **kwargs)
        #self.fields['current_date'].initial = d

    def __init__(self, *args, **kwargs):
        kwargs.update(initial={
            'current_time': datetime.datetime.now()+datetime.timedelta(minutes=30),
            'current_date': datetime.date.today()
        })
        super(Order, self).__init__(*args, **kwargs)

    def clean_current_time(self, *args, **kwargs):
        current_time = self.cleaned_data.get('current_time')
        if current_time < datetime.time(hour=8, minute=0, second=0, microsecond=0, tzinfo=None) or current_time > datetime.time(hour=20, minute=0, second=0, microsecond=0, tzinfo=None):
            raise forms.ValidationError('Введите, пожалуйста, требуемое время парковки в рабочие часы с 8:00 до 20:00')
        return current_time

    def clean_current_date(self, *args, **kwargs):
        current_date = self.cleaned_data.get('current_date')
        if current_date < d:
            raise forms.ValidationError('Введите, пожалуйста, дату сегодня или позднее')
        elif current_date.weekday() == 5:
            raise forms.ValidationError('Выберите, пожалуйста, будний день')
        elif current_date.weekday() == 6:
            raise forms.ValidationError('Выберите, пожалуйста, будний день')
        return current_date


class CallBack2(forms.Form):
    name = forms.CharField(label='Ваше Имя', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ваше имя'}), max_length=100, required=False)
    phone = forms.CharField(label='Телефон', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Введите номер телефона'}), max_length=11, required = True)
