from django.forms import Modelform, CharField, IntegerField

class PersonForm(ModelForm):
    name = CharField(label='Введите имя')
    age = IntegerField(label='Введите возраст')

    class Meta:
        model = Person
        fields = ['name', 'age']