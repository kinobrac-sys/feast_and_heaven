from django import forms
from hunger.models import Shopcart, Reservation

class ShopcartForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShopcartForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Shopcart
        fields = ['item', 'quantity']


class CartFilterForm(forms.Form):
    category_choise = [
        ('', 'All categories'),
        ("Перше блюдо", "Перше блюдо"),
        ("Друге блюдо", "Друге блюдо"),
        ("Десерт", "Десерт"),
        ("Напій", "Напій"),
        ("Закуска", "Закуска"),
        ("Салат", "Салат"),
        ("Гостра", "Гостра"),
    ]
    category = forms.ChoiceField(choices=category_choise, label='Category', required=False)
    def __init__(self, *args, **kwargs):
        super(CartFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-select'})
