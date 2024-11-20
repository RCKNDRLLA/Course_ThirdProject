from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(label='Введите имя')
    age = forms.CharField(label='Введите возраст')

